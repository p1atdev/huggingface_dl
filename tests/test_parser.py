import unittest
from huggingface_dl.parser import HfURLParser


class HfURLParserTest(unittest.TestCase):
    def test_model_repo_without_file_path(self):
        parsed = HfURLParser("https://huggingface.co/google/flan-ul2")
        self.assertEqual(parsed.parsed_url["repo_type"], "model")
        self.assertEqual(parsed.parsed_url["repo_id"], "google/flan-ul2")
        self.assertEqual(parsed.parsed_url["revision"], None)
        self.assertEqual(parsed.parsed_url["file_path"], "")
        self.assertEqual(parsed.parsed_url["is_folder"], True)

    def test_model_repo_with_file_path_blob_url(self):
        parsed = HfURLParser(
            "https://huggingface.co/facebook/sam-vit-huge/blob/main/pytorch_model.bin"
        )
        self.assertEqual(parsed.parsed_url["repo_type"], "model")
        self.assertEqual(parsed.parsed_url["repo_id"], "facebook/sam-vit-huge")
        self.assertEqual(parsed.parsed_url["revision"], "main")
        self.assertEqual(parsed.parsed_url["file_path"], "pytorch_model.bin")
        self.assertEqual(parsed.parsed_url["is_folder"], False)

    def test_model_repo_with_file_path_resolve_url(self):
        parsed = HfURLParser(
            "https://huggingface.co/lllyasviel/ControlNet/resolve/main/training/fill50k.zip"
        )
        self.assertEqual(parsed.parsed_url["repo_type"], "model")
        self.assertEqual(parsed.parsed_url["repo_id"], "lllyasviel/ControlNet")
        self.assertEqual(parsed.parsed_url["revision"], "main")
        self.assertEqual(parsed.parsed_url["file_path"], "training/fill50k.zip")
        self.assertEqual(parsed.parsed_url["is_folder"], False)

    def test_model_repo_with_file_path_tree_url(self):
        parsed = HfURLParser(
            "https://huggingface.co/runwayml/stable-diffusion-v1-5/tree/main/unet"
        )
        self.assertEqual(parsed.parsed_url["repo_type"], "model")
        self.assertEqual(parsed.parsed_url["repo_id"], "runwayml/stable-diffusion-v1-5")
        self.assertEqual(parsed.parsed_url["revision"], "main")
        self.assertEqual(parsed.parsed_url["file_path"], "unet")
        self.assertEqual(parsed.parsed_url["is_folder"], True)

    def test_datasets_repo_without_file_path(self):
        parsed = HfURLParser("https://huggingface.co/datasets/laion/laion-art")
        self.assertEqual(parsed.parsed_url["repo_type"], "datasets")
        self.assertEqual(parsed.parsed_url["repo_id"], "laion/laion-art")
        self.assertEqual(parsed.parsed_url["revision"], None)
        self.assertEqual(parsed.parsed_url["file_path"], "")
        self.assertEqual(parsed.parsed_url["is_folder"], True)

    def test_datasets_repo_with_file_path_blob_url(self):
        parsed = HfURLParser(
            "https://huggingface.co/datasets/laion/laion400m_new/blob/main/0000.parquet"
        )
        self.assertEqual(parsed.parsed_url["repo_type"], "datasets")
        self.assertEqual(parsed.parsed_url["repo_id"], "laion/laion400m_new")
        self.assertEqual(parsed.parsed_url["revision"], "main")
        self.assertEqual(parsed.parsed_url["file_path"], "0000.parquet")
        self.assertEqual(parsed.parsed_url["is_folder"], False)

    def test_spaces_repo_without_file_path(self):
        parsed = HfURLParser("https://huggingface.co/spaces/Salesforce/BLIP2")
        self.assertEqual(parsed.parsed_url["repo_type"], "spaces")
        self.assertEqual(parsed.parsed_url["repo_id"], "Salesforce/BLIP2")
        self.assertEqual(parsed.parsed_url["revision"], None)
        self.assertEqual(parsed.parsed_url["file_path"], "")
        self.assertEqual(parsed.parsed_url["is_folder"], True)


if __name__ == "__main__":
    unittest.main()
