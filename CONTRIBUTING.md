# Contributing Guide

Thank you for your interest in contributing to OCR Invoice Reader GUI!

---

## Ways to Contribute

- 🐛 **Report bugs** - Help us identify issues
- 💡 **Suggest features** - Share your ideas
- 📝 **Improve documentation** - Make it clearer
- 💻 **Submit code** - Fix bugs or add features
- 🌍 **Translate** - Help with internationalization

---

## Before You Start

1. **Check existing issues** - Avoid duplicates
2. **Read documentation** - Understand the project
3. **Test locally** - Verify your changes work

---

## Reporting Bugs

### Good Bug Report

Include:
- **Description** - What happened vs. what should happen
- **Steps to reproduce** - Exact steps to trigger bug
- **Environment**:
  - OS version
  - Python version
  - Package versions
- **Error messages** - Full error output
- **Screenshots** - If applicable

### Example

```markdown
**Bug:** GUI crashes when processing large PDF

**Steps:**
1. Start GUI
2. Select 100-page PDF file
3. Click "Process Document"
4. GUI crashes after 5 seconds

**Environment:**
- Windows 10
- Python 3.10.0
- ocr-invoice-reader 2.0.0

**Error:**
MemoryError: Unable to allocate array
...
```

---

## Suggesting Features

### Good Feature Request

Include:
- **Use case** - Why is this needed?
- **Description** - What should it do?
- **Examples** - How would it work?
- **Alternatives** - What do you do now?

### Example

```markdown
**Feature:** Batch processing mode

**Use case:** I need to process 50 invoices daily

**Description:** Add button to select multiple files at once

**Example:**
1. Click "Batch Process"
2. Select multiple files
3. Process all automatically

**Current workaround:**
Process files one by one manually
```

---

## Code Contributions

### Setup Development Environment

```bash
# Fork and clone repository
git clone https://github.com/YOUR_USERNAME/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui

# Install dependencies
cd ../ocr-invoice-reader
pip install -e .

# Test
cd ../ocr-invoice-reader-gui
python src/ocr_gui_simple.py
```

### Coding Standards

**Style:**
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions
- Keep functions short and focused

**Example:**
```python
def process_document(file_path: str) -> dict:
    """
    Process document using OCR engine.

    Args:
        file_path: Path to document file

    Returns:
        Dictionary with OCR results

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format unsupported
    """
    # Implementation
    pass
```

### Making Changes

1. **Create branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make changes:**
   - Edit code
   - Test thoroughly
   - Update documentation

3. **Commit:**
   ```bash
   git add .
   git commit -m "Add: Brief description of change"
   ```

   **Commit message format:**
   - `Add: ...` - New feature
   - `Fix: ...` - Bug fix
   - `Update: ...` - Improve existing
   - `Remove: ...` - Delete code
   - `Refactor: ...` - Code restructure
   - `Docs: ...` - Documentation only

4. **Push:**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request:**
   - Go to GitHub
   - Click "New Pull Request"
   - Fill in description
   - Link related issues

### Pull Request Checklist

- [ ] Code follows style guidelines
- [ ] Changes tested locally
- [ ] Documentation updated
- [ ] Commit messages clear
- [ ] No merge conflicts
- [ ] Related issues linked

---

## Documentation

### Improving Docs

Documentation lives in:
- `README.md` - Project overview
- `docs/INSTALL.md` - Installation guide
- `docs/TROUBLESHOOTING.md` - Common issues
- `CHANGELOG.md` - Version history

**Guidelines:**
- Use clear, simple language
- Include code examples
- Add screenshots if helpful
- Keep formatting consistent

---

## Testing

### Manual Testing

Before submitting:

1. **GUI starts:**
   ```bash
   python src/ocr_gui_simple.py
   ```

2. **File selection works:**
   - Browse button opens dialog
   - Selected file shows in label

3. **Processing works:**
   - First file: OCR loads (~10s)
   - Subsequent: Fast (~3s)
   - Results display correctly

4. **Edge cases:**
   - Very large files
   - Corrupted files
   - Multiple file types

### Test on Multiple Platforms

If possible, test on:
- Windows 10/11
- macOS
- Linux (Ubuntu)

---

## Questions?

- **General questions**: Create a Discussion
- **Bug reports**: Create an Issue
- **Security issues**: Email maintainer privately

---

## Code of Conduct

### Be Respectful

- Respectful communication
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for project

### Not Tolerated

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

---

## Recognition

Contributors will be:
- Listed in release notes
- Credited in documentation
- Appreciated by community

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Thank You! 🎉

Every contribution helps make this project better for everyone.

---

## Links

- **Issues**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues
- **Pull Requests**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/pulls
- **Discussions**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/discussions
