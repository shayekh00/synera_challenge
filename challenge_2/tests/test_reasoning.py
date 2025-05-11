# Unit test for reasoning agent

import unittest
from reasoning_agent import ReasoningAgent

class TestReasoningAgent(unittest.TestCase):

    def setUp(self):
        self.agent = ReasoningAgent()

    def test_reasoning(self):
        input_data = "some input data"
        expected_output = "expected output"
        self.assertEqual(self.agent.reason(input_data), expected_output)

    def test_another_reasoning_case(self):
        input_data = "another input data"
        expected_output = "another expected output"
        self.assertEqual(self.agent.reason(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()