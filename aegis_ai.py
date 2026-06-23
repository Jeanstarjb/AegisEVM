import os
import sys
import argparse
from google import genai
from google.genai import types

def run_ai_explanation(vulnerability_text: str, source_code: str = None) -> str:
    """Sends the raw vulnerability output to Gemini to get a human-readable explanation and fix."""
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return "⚠️ Error: GOOGLE_API_KEY environment variable is not set. Cannot run AI Explainer."

    client = genai.Client()
    
    prompt = f"""
    You are an elite Smart Contract Security Auditor for 'AegisEVM'.
    The symbolic execution engine has just detected a vulnerability in a smart contract.
    
    Here is the raw output from the engine:
    {vulnerability_text}
    """
    
    if source_code:
        prompt += f"""
        Here is the source code of the contract:
        ```solidity
        {source_code}
        ```
        """
        
    prompt += """
    Your task:
    1. Explain exactly how a hacker would exploit this vulnerability in simple terms.
    2. Provide the corrected Solidity code to fix this issue.
    Format your response beautifully in Markdown. Do not include pleasantries.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        return response.text
    except Exception as e:
        return f"⚠️ AI Explanation Failed: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AegisEVM AI Explainer")
    parser.add_argument("--log", required=True, help="Raw mythril output log text")
    parser.add_argument("--source", required=False, help="Path to the original .sol file")
    
    args = parser.parse_args()
    
    log_text = args.log
    source_text = None
    
    if args.source and os.path.exists(args.source):
        with open(args.source, 'r') as f:
            source_text = f.read()
            
    print("🧠 Requesting AI Analysis from Neural Core...")
    explanation = run_ai_explanation(log_text, source_text)
    
    print("\n" + "="*50)
    print("🛡️ AEGIS AI ANALYSIS")
    print("="*50)
    print(explanation)
