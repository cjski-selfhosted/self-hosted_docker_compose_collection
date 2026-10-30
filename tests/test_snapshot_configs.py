import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).parents[1] / 'tools/snapshot_configs.py'
spec = importlib.util.spec_from_file_location('snapshot_configs', MODULE)
snapshot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(snapshot)

class SnapshotBoundaryTests(unittest.TestCase):
    def test_output_inside_collection_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'collection';root.mkdir()
            with self.assertRaises(ValueError):snapshot.validate_output(root/'backups'/'one',root)
    def test_output_symlink_into_collection_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)/'collection';root.mkdir();alias=Path(tmp)/'alias';alias.symlink_to(root,target_is_directory=True)
            with self.assertRaises(ValueError):snapshot.validate_output(alias/'backup',root)
    def test_private_files_are_owner_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'private'/'config.txt';snapshot.write_private(path,b'synthetic-secret')
            self.assertEqual(path.stat().st_mode & 0o777,0o600)
            self.assertEqual(path.parent.stat().st_mode & 0o777,0o700)
    def test_private_files_cannot_be_overwritten_silently(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'config';snapshot.write_private(path,b'first')
            with self.assertRaises(FileExistsError):snapshot.write_private(path,b'second')
            self.assertEqual(path.read_bytes(),b'first')
    def test_export_into_another_git_repo_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            collection=Path(tmp)/'collection';collection.mkdir();other=Path(tmp)/'other';other.mkdir();(other/'.git').mkdir()
            with self.assertRaises(ValueError):snapshot.validate_output(other/'backup',collection)

if __name__=='__main__':unittest.main()
