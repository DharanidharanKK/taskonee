# Folder Naming Guide - Document360 API

## Issue: 400 Bad Request Error

When you see this error:
```
2026-01-13 09:38:24,308 - WARNING - Non-success response received: 400
2026-01-13 09:38:24,309 - ERROR - Bad Request - Invalid parameters for POST Create Folder
Failed to create folder: My-Test-Folder
```

It means the API rejected the folder name format.

---

## Allowed Characters

✅ **Use these characters:**
- Letters (a-z, A-Z)
- Numbers (0-9)
- Spaces
- Hyphens (-)
- Underscores (_)
- Periods (.)

❌ **Avoid these characters:**
- Slashes: / \
- Angle brackets: < >
- Colons: :
- Quotes: " '
- Pipes: |
- Question marks: ?
- Asterisks: *

---

## Working Examples

| Folder Name | Status | Reason |
|-------------|--------|--------|
| My Documents | ✅ | Letters and spaces |
| Project 2026 | ✅ | Alphanumeric with spaces |
| Team_Files | ✅ | Underscore allowed |
| Project-Alpha | ✅ | Hyphen allowed |
| Archive.2025 | ✅ | Period allowed |
| My-Test-Folder | ❌ | May fail (try "My Test Folder" instead) |
| My/Documents | ❌ | Forward slash not allowed |
| File:Archive | ❌ | Colon not allowed |
| Data\\Backup | ❌ | Backslash not allowed |

---

## Common Issues & Solutions

### Issue 1: Dashes in Folder Name
**Problem:** Folder name with dashes like "My-Test-Folder"  
**Solution:** Use spaces or underscores instead
```
✅ Good:    "My Test Folder"
✅ Good:    "My_Test_Folder"
❌ Problem: "My-Test-Folder"
```

### Issue 2: Special Characters
**Problem:** Using symbols like @, #, $, etc.  
**Solution:** Remove or replace with allowed characters
```
❌ Bad:  "Project@2026"
✅ Good: "Project 2026"

❌ Bad:  "Files#Archive"
✅ Good: "Files Archive"
```

### Issue 3: Leading/Trailing Spaces
**Problem:** Folder name with spaces at start/end  
**Solution:** Application automatically strips these, but avoid them
```
❌ Bad:  " My Folder "  (spaces at ends)
✅ Good: "My Folder"
```

---

## How the Application Validates

The application now validates folder names before sending to the API:

```python
validate_folder_name("My Folder")        # ✅ PASS
validate_folder_name("Project-2026")     # ⚠️ May fail at API
validate_folder_name("My/Folder")        # ❌ FAIL (invalid char /)
validate_folder_name("")                 # ❌ FAIL (empty)
validate_folder_name("A" * 256)          # ❌ FAIL (too long)
```

If validation fails, you'll see a clear error message before the API call is made.

---

## Testing

### Test 1: Simple Name
```
Folder name: My Documents
Expected: ✅ Success
```

### Test 2: With Numbers
```
Folder name: Project 2026
Expected: ✅ Success
```

### Test 3: With Underscores
```
Folder name: Team_Files
Expected: ✅ Success
```

### Test 4: With Spaces
```
Folder name: Archive Documents 2025
Expected: ✅ Success
```

---

## Error Messages

### Validation Errors (Before API Call)

```
Invalid folder name format: Folder name cannot be empty
→ Solution: Provide a folder name

Invalid folder name format: Folder name contains invalid character: '/'
→ Solution: Use "My Documents" instead of "My/Documents"

Invalid folder name format: Folder name cannot exceed 255 characters
→ Solution: Use a shorter name
```

### API Errors (400 Bad Request)

```
Bad Request - The API rejected the folder name format
Try using alphanumeric characters, spaces, hyphens, and underscores only
Example: 'My Folder', 'Project-2026', 'Team_Documents'
```

---

## Step-by-Step Example

1. **Run Application:**
   ```powershell
   python task_app.py
   ```

2. **Provide API Token:**
   ```
   [API Token Setup]
   Enter your API token: [paste your token]
   ✓ API token configured successfully
   ```

3. **Try Creating Folder:**
   ```
   [0.5] POST Create Folder - Creating a new folder in Document360 API
   (Tip: Use alphanumeric characters, spaces, hyphens, and underscores)
   (Example: 'My Folder', 'Project-2026', 'Team_Documents')
   Enter folder name to create: My New Folder
   ```

4. **Success Response:**
   ```
   ✓ Folder created successfully!
     Folder ID: abc123
     Folder Name: My New Folder
   ```

---

## More Help

If you continue to get errors:

1. **Check the logs:** Open `api_requests.log` to see exact request/response
2. **Simplify the name:** Try a very simple name like "Test"
3. **Contact support:** If the issue persists, your API token may have restrictions

---

## Summary

- ✅ Use: Letters, numbers, spaces, hyphens, underscores, periods
- ❌ Avoid: Special characters, slashes, colons, quotes, pipes, asterisks
- ⚠️ Hyphens may cause issues in some cases - prefer spaces or underscores
- 🔍 Check logs for detailed error messages
