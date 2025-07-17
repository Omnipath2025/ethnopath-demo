Here's the test file content to copy and paste:
#!/usr/bin/env python3
"""
Test suite for EthnoPath traditional knowledge digitization.
Ensures ethical compliance and functionality validation.
© 2025 Cloak and Quill Research - 501(c)(3) Public Charity
"""
import unittest
import sys
import os
Add the demo directory to the path so we can import the demo module
sys.path.insert(0, os.path.join(os.path.dirname(file), '..', 'demo'))
try:
from traditional_knowledge_demo import TraditionalKnowledgeProcessor, EthnoPathDemo
except ImportError:
print("Warning: Could not import demo modules. Ensure demo script exists.")
class TestTraditionalKnowledgeProcessor(unittest.TestCase):
"""Test the core traditional knowledge processing functionality."""
def setUp(self):
    """Set up test fixtures."""
    self.processor = TraditionalKnowledgeProcessor()

def test_ethical_guidelines_enforcement(self):
    """Test that ethical guidelines are properly enforced."""
    guidelines = self.processor.ethical_guidelines
    
    # Verify all ethical guidelines are enabled
    self.assertTrue(guidelines["public_knowledge_only"])
    self.assertTrue(guidelines["cultural_respect"])
    self.assertTrue(guidelines["attribution_required"])
    self.assertTrue(guidelines["sacred_knowledge_excluded"])

def test_audio_processing(self):
    """Test audio knowledge processing functionality."""
    plant_name = "Test Plant"
    audio_description = "Traditional healing plant used for wellness"
    
    result = self.processor.process_audio_knowledge(plant_name, audio_description)
    
    # Verify expected fields are present
    self.assertIn("spoken_content", result)
    self.assertIn("cultural_context", result)
    self.assertIn("preservation_quality", result)
    self.assertIn("audio_clarity", result)
    
    # Verify quality metrics
    self.assertGreater(result["preservation_quality"], 0.9)
    self.assertEqual(result["spoken_content"], audio_description)

def test_visual_processing(self):
    """Test visual knowledge processing functionality."""
    plant_name = "Test Plant"
    visual_description = "Green leaves with healing properties"
    
    result = self.processor.process_visual_knowledge(plant_name, visual_description)
    
    # Verify expected fields are present
    self.assertIn("plant_identification", result)
    self.assertIn("preparation_methods", result)
    self.assertIn("cultural_significance", result)
    self.assertIn("visual_accuracy", result)
    
    # Verify accuracy metrics
    self.assertGreater(result["visual_accuracy"], 0.9)

def test_textual_processing(self):
    """Test textual knowledge processing functionality."""
    plant_name = "Test Plant"
    traditional_uses = ["healing", "wellness", "traditional medicine"]
    
    result = self.processor.process_textual_knowledge(plant_name, traditional_uses)
    
    # Verify expected fields are present
    self.assertIn("documented_uses", result)
    self.assertIn("cultural_context", result)
    self.assertIn("knowledge_source", result)
    self.assertIn("text_preservation", result)
    
    # Verify preservation quality
    self.assertGreater(result["text_preservation"], 0.95)
    self.assertEqual(result["documented_uses"], traditional_uses)

def test_knowledge_graph_creation(self):
    """Test knowledge graph creation functionality."""
    test_plant_data = {
        "name": "Test Plant",
        "uses": ["healing", "wellness"],
        "preparation": "Traditional brewing method"
    }
    
    result = self.processor.create_knowledge_graph(test_plant_data)
    
    # Verify expected fields are present
    self.assertIn("plant_name", result)
    self.assertIn("traditional_uses", result)
    self.assertIn("preparation_methods", result)
    self.assertIn("cultural_relationships", result)
    self.assertIn("relationship_integrity", result)
    
    # Verify data integrity
    self.assertEqual(result["plant_name"], test_plant_data["name"])
    self.assertEqual(result["traditional_uses"], test_plant_data["uses"])
    self.assertGreater(result["relationship_integrity"], 0.9)
class TestEthnoPathDemo(unittest.TestCase):
"""Test the main EthnoPath demonstration functionality."""
def setUp(self):
    """Set up demo test fixtures."""
    self.demo = EthnoPathDemo()

def test_demo_initialization(self):
    """Test that demo initializes properly."""
    self.assertIsNotNone(self.demo.processor)
    self.assertIsNotNone(self.demo.demo_plants)
    self.assertGreater(len(self.demo.demo_plants), 0)

def test_sample_plants_data_integrity(self):
    """Test that sample plant data maintains required structure."""
    for plant in self.demo.demo_plants:
        # Verify required fields are present
        required_fields = ["name", "scientific_name", "uses", "preparation", 
                         "audio_description", "visual_description"]
        
        for field in required_fields:
            self.assertIn(field, plant, f"Missing field: {field}")
            self.assertIsNotNone(plant[field], f"Null field: {field}")

def test_ethical_compliance_verification(self):
    """Test that all sample data maintains ethical boundaries."""
    for plant in self.demo.demo_plants:
        # Verify only public knowledge is included
        plant_name = plant["name"]
        
        # These are well-known, publicly documented plants
        public_plants = ["Aloe Vera", "Chamomile", "Lavender"]
        self.assertIn(plant_name, public_plants, 
                     f"Plant {plant_name} should be publicly documented knowledge only")

def test_processing_performance_metrics(self):
    """Test that processing maintains expected performance levels."""
    # Test with a single plant to verify metrics
    test_plant = self.demo.demo_plants[0]
    
    audio_result = self.demo.processor.process_audio_knowledge(
        test_plant["name"], test_plant["audio_description"]
    )
    
    # Verify performance thresholds
    self.assertGreaterEqual(audio_result["preservation_quality"], 0.94)
class TestEthicalCompliance(unittest.TestCase):
"""Dedicated tests for ethical compliance verification."""
def test_public_knowledge_only_policy(self):
    """Verify that only public domain knowledge is processed."""
    processor = TraditionalKnowledgeProcessor()
    
    # Verify ethical guidelines enforce public knowledge only
    self.assertTrue(processor.ethical_guidelines["public_knowledge_only"])
    self.assertTrue(processor.ethical_guidelines["sacred_knowledge_excluded"])

def test_cultural_respect_framework(self):
    """Verify cultural respect framework is active."""
    processor = TraditionalKnowledgeProcessor()
    
    # Verify cultural respect and attribution requirements
    self.assertTrue(processor.ethical_guidelines["cultural_respect"])
    self.assertTrue(processor.ethical_guidelines["attribution_required"])

def test_no_sacred_content_processing(self):
    """Verify that sacred or sensitive content is excluded."""
    demo = EthnoPathDemo()
    
    # Verify all demo plants are safe, public knowledge
    safe_plants = ["Aloe Vera", "Chamomile", "Lavender"]
    
    for plant in demo.demo_plants:
        self.assertIn(plant["name"], safe_plants, 
                     "Only safe, public domain plants should be included")
def run_tests():
"""Run all EthnoPath tests with detailed output."""
print("🧪 Running EthnoPath Test Suite")
print("=" * 50)
print("🔒 Verifying ethical compliance and functionality")
print()
# Create test suite
test_suite = unittest.TestSuite()

# Add all test classes
test_classes = [
    TestTraditionalKnowledgeProcessor,
    TestEthnoPathDemo,
    TestEthicalCompliance
]

for test_class in test_classes:
    tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
    test_suite.addTests(tests)

# Run tests with detailed output
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(test_suite)

# Print summary
print()
print("📊 TEST SUMMARY")
print("=" * 30)
print(f"Tests Run: {result.testsRun}")
print(f"Failures: {len(result.failures)}")
print(f"Errors: {len(result.errors)}")

if result.wasSuccessful():
    print("✅ All tests passed! EthnoPath maintains ethical compliance.")
else:
    print("❌ Some tests failed. Please review ethical compliance.")

return result.wasSuccessful()
if name == "main":
success = run_tests()
sys.exit(0 if success else 1)
