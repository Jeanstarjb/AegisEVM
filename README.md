# 🛡️ AegisEVM

> **"Code is law. Aegis is the enforcer."**

Welcome to **AegisEVM**, the premier symbolic-execution-based security auditor for Ethereum and EVM-compatible smart contracts. 

In a decentralized world where a single unhandled exception can drain millions of dollars in a flash-loan attack, AegisEVM stands as your digital immune system. It mathematically computes all possible execution paths of your Solidity bytecode to detect vulnerabilities *before* you deploy.

## ⚡ The Armory (Features)

AegisEVM doesn't just look for typos. It executes a full symbolic analysis graph on your bytecode to detect critical Web3 attack vectors:

- **Reentrancy Detection:** Maps out complex cross-contract state changes to prevent DAO-style recursive drains.
- **Integer Overflow/Underflow:** Mathematically proves if your math can be manipulated to mint infinite tokens.
- **Unprotected Self-Destructs:** Ensures nobody but you can call `selfdestruct()` and kill your contract.
- **Oracle Manipulation:** Traces paths to see if flash-loans can break your price feeds.
- **Authorization Bypasses:** Finds backdoor logic that grants attackers admin rights.

---

## 🖥️ The Aegis Dashboard (Web UI)

Stop reading terminal logs. AegisEVM comes with a sleek, built-in visual dashboard for auditing contracts via your browser.

**To launch the dashboard:**
```bash
# Ensure streamlit is installed
pip install streamlit mythril

# Run the Aegis UI
streamlit run aegis_dashboard.py
```
*Drag and drop your `.sol` files into the dashboard and hit launch for a visual audit report.*

---

## 🧠 Neural Core (AI Explainer)

When Aegis detects a vulnerability, it outputs dense execution traces. If you want the exploit explained in plain English—and the patched code written for you—invoke the Neural Core.

**To run the AI Explainer:**
```bash
# Ensure google-genai is installed
pip install google-genai

# Export your API key
export GOOGLE_API_KEY="your-api-key"

# Pipe your audit log into the explainer
myth analyze target.sol > audit.log
python aegis_ai.py --log audit.log --source target.sol
```

---

## ⚙️ Automated CI/CD (GitHub Actions)

AegisEVM includes a pre-configured GitHub Action to automatically audit your entire repository on every Pull Request. 

If a developer tries to merge vulnerable code, AegisEVM will instantly block the PR. The workflow is located at `.github/workflows/aegis-audit.yml`.

---

> **"Deploy with absolute mathematical certainty."**
> — *The AegisEVM Collective*
