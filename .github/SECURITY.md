# Security Policy

## Supported Versions

We are committed to maintaining the security of `PyDataFlow-Automated-Data-Pipeline-CLI-Tool`. We actively monitor and address security vulnerabilities in the following versions:

| Version | Supported          |
|---------|--------------------|
| Latest  | :white_check_mark: |


## Reporting a Vulnerability

We take security vulnerabilities very seriously. If you discover a security issue, please report it to us promptly via email at <security@example.com> or by opening a [Security Advisory](https://github.com/chirag127/PyDataFlow-Automated-Data-Pipeline-CLI-Tool/security/advisories/new). Please do **not** disclose the vulnerability publicly until it has been addressed.

We request that you do the following:

*   **Email Disclosure:** Send a detailed email to <security@example.com> with the subject line "Security Vulnerability Report".
*   **GitHub Advisory:** Open a new Security Advisory in our GitHub repository: [chirag127/PyDataFlow-Automated-Data-Pipeline-CLI-Tool](https://github.com/chirag127/PyDataFlow-Automated-Data-Pipeline-CLI-Tool/security/advisories/new).

We will acknowledge receipt of your vulnerability report within **48 hours** and will make every effort to respond and address the issue promptly.

## Vulnerability Disclosure Policy

Once we receive a security vulnerability report, we will:

1.  Acknowledge receipt of the report.
2.  Assess the vulnerability's impact and severity.
3.  Develop a patch or mitigation strategy.
4.  Notify the reporter when the vulnerability is resolved.
5.  Publicly disclose the vulnerability (after resolution) as appropriate, crediting the reporter.

## Development Practices

To minimize security risks, `PyDataFlow-Automated-Data-Pipeline-CLI-Tool` adheres to the following secure development practices:

*   **Dependency Management:** We use `uv` for managing dependencies and regularly scan for vulnerabilities using tools integrated into our CI pipeline.
*   **Code Linting & Formatting:** `Ruff` is used to enforce code quality and identify potential security anti-patterns.
*   **Testing:** Comprehensive test suites using `Pytest` help ensure the integrity and security of the codebase.
*   **Input Validation:** All external inputs to the CLI are validated to prevent injection attacks.
*   **Principle of Least Privilege:** The tool operates with the minimum necessary permissions.

---

Thank you for helping to keep `PyDataFlow-Automated-Data-Pipeline-CLI-Tool` secure!
