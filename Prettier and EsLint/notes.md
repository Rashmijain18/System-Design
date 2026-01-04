# 1️⃣ First: What problem do they solve?

### Without ESLint / Prettier

- Inconsistent code styles across team
- Hidden bugs (unused vars, wrong dependencies, unsafe patterns)
- PR comments like:

  > “Please format this”
  > “Why is this variable unused?”
  > “This will break in strict mode”

---

# 2️⃣ ESLint vs Prettier (VERY IMPORTANT)

| Tool         | Purpose                        | What it cares about                |
| ------------ | ------------------------------ | ---------------------------------- |
| **ESLint**   | Code **quality & correctness** | Bugs, bad patterns, best practices |
| **Prettier** | Code **formatting**            | Spaces, semicolons, line breaks    |

---

# 3️⃣ ESLint – Deep Dive

“ESLint parses JavaScript into an AST, applies rule-based checks on that AST to detect bugs, bad practices, and inconsistencies, and then reports or auto-fixes issues depending on the rule configuration.”

## What ESLint actually does

ESLint:

1. Parses your JS/TS code into an **AST** (Abstract Syntax Tree)
2. Runs **rules** on that AST
3. Reports **errors or warnings**

# What is an AST?

# AST = Abstract Syntax Tree

It’s a tree representation of your code’s structure.

Example code
const sum = (a, b) => a + b;

Simplified AST (conceptual)
Program
└── VariableDeclaration (const)
├── Identifier (sum)
└── ArrowFunctionExpression
├── Params: a, b
└── BinaryExpression (+)
├── Identifier (a)
└── Identifier (b)

# Why ESLint needs AST

ESLint does not read text
It understands meaning, not characters

Example: Why AST matters
if (true) {
return;
console.log("hello");
}

ESLint sees:
return node

followed by console.log
➡ unreachable code

❌ This cannot be detected by regex
✔ AST makes it possible

---

## Common ESLint rule categories

### 1. **Possible Errors**

- `no-undef`
- `no-unreachable`
- `no-extra-semi`

### 2. **Best Practices**

- `eqeqeq`
- `no-eval`
- `curly`

if (x == 5) {
console.log("hi");
}

ESLint sees BinaryExpression Operator: ==

❌ Error:
Expected '===' and instead saw '=='

### 3. **Variables**

- `no-unused-vars`
- `no-shadow`

function greet(name) {
const message = "Hello";
return name;
}

ESLint Tracks references -> Sees zero usage

❌ ESLint error:
'message' is assigned a value but never used

### 4. **ES6+**

- `prefer-const`
- `no-var`

### 5. **Framework-specific**

- React
- Next.js
- Node.js

function MyComponent() {
return <div>Hello</div>
❌ Error if missing - import React from "react"; - Older React required:

---

## ESLint Config File Types

You’ll see one of these:

- `.eslintrc.json`
- `.eslintrc.js`
- `.eslintrc.cjs`
- `eslint.config.js` (new flat config)

### Typical ESLint config (React + TS)

```js
module.exports = {
  env: {
    browser: true,
    es2021: true,
    node: true,
  },
  parser: "@typescript-eslint/parser",
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module",
  },
  plugins: ["@typescript-eslint", "react"],
  extends: [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:@typescript-eslint/recommended",
  ],
  rules: {
    "no-console": "warn",
    "@typescript-eslint/no-unused-vars": ["error"],
    "react/react-in-jsx-scope": "off",
  },
};
```

---

## ESLint severity levels

```js
"rule-name": "off" | "warn" | "error"
```

Example:

```js
"no-console": "warn"
```

---

# 4️⃣ Prettier – Deep Dive

## What Prettier does

- Takes your code
- Reprints it in a **consistent format**
- No AST logic checks
- No opinions about correctness

### Example

**Before**

```js
function sum(a, b) {
  return a + b;
}
```

**After (Prettier)**

```js
function sum(a, b) {
  return a + b;
}
```

---

## Prettier Config

`.prettierrc`

```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "trailingComma": "es5",
  "printWidth": 80
}
```

### Key options explained

| Option          | Meaning           |
| --------------- | ----------------- |
| `semi`          | semicolons or not |
| `singleQuote`   | ' vs "            |
| `tabWidth`      | indentation       |
| `printWidth`    | line length       |
| `trailingComma` | safer diffs       |

---

# Why ESLint & Prettier Conflict

## Short answer (memorize this)

> **They both try to format code, but with different rules and opinions.**

Now let’s **prove this with examples**.

---

## 1️⃣ ESLint was originally doing **two jobs**

Historically ESLint handled:

1. **Code correctness** (bugs, bad patterns)
2. **Code style/formatting** (indentation, quotes, spacing)

Prettier came later and said:

> “I’ll handle formatting. Only formatting.”

⚠️ Problem: ESLint already had formatting rules.

---

## 2️⃣ Example: Indentation conflict

### ESLint rule

```js
"indent": ["error", 2]
```

### Prettier config

```json
{
  "tabWidth": 4
}
```

---

### Code

```js
function test() {
  console.log("hi");
}
```

#### What happens

- Prettier says ✅ (4 spaces is correct)
- ESLint says ❌ (expects 2 spaces)

➡️ **Same line, opposite opinions**

---

## 3️⃣ Example: Quotes conflict

### ESLint rule

```js
"quotes": ["error", "single"]
```

### Prettier config

```json
{
  "singleQuote": false
}
```

---

### Code

```js
const name = "Rashmi";
```

- Prettier → keeps double quotes
- ESLint → errors

---

## 4️⃣ Example: Semicolons conflict

### ESLint

```js
"semi": ["error", "always"]
```

### Prettier

```json
{
  "semi": false
}
```

---

### Code

```js
const x = 10;
```

- Prettier → removes semicolon
- ESLint → demands semicolon

---

## 5️⃣ Example: Line length conflict

### ESLint

```js
"max-len": ["error", 80]
```

### Prettier

```json
{
  "printWidth": 100
}
```

---

### Code

```js
const message =
  "This is a very long string that goes beyond eighty characters but still acceptable for prettier";
```

- Prettier → allows it
- ESLint → errors

---

## 6️⃣ Why this becomes painful in real projects

### Symptoms you’ll see

- ESLint errors immediately after Prettier runs
- Code flips back and forth on save
- Endless PR comments
- Devs disable rules randomly 😬

---

## 7️⃣ Root Cause (Important)

> **ESLint rules operate on AST logic + style**
>
> **Prettier ignores rules and reprints code**

They do **not coordinate** unless you tell them to.

---

## 8️⃣ The Correct Fix (Industry Standard)

### Rule #1

> **Only one tool formats code**

🔥 That tool = **Prettier**

---

### Step 1: Disable ESLint formatting rules

Install:

```bash
npm install -D eslint-config-prettier
```

This package:

- Turns **off** ESLint rules that conflict with Prettier
- Includes: `indent`, `quotes`, `semi`, `max-len`, etc.

---

### Step 2: Let ESLint run Prettier

Install:

```bash
npm install -D eslint-plugin-prettier
```

Now Prettier runs **as an ESLint rule**.

---

### Step 3: Correct ESLint config

```js
extends: [
  "eslint:recommended",
  "plugin:@typescript-eslint/recommended",
  "plugin:prettier/recommended"
]
```

What this does:

- Disables ESLint formatting rules
- Runs Prettier last
- Reports formatting issues as ESLint errors

---

## 9️⃣ Visual Mental Model (Remember This)

```
Before:
ESLint → format
Prettier → format
❌ Conflict

After:
Prettier → format
ESLint → logic & bugs
✅ Peace
```

---

## 🔟 Interview-ready explanation (memorize)

> “ESLint and Prettier conflict because both attempt to enforce code formatting. ESLint historically included formatting rules, while Prettier enforces its own opinionated formatting. The conflict is resolved by disabling ESLint’s formatting rules using eslint-config-prettier and letting Prettier handle formatting exclusively.”

# 7️⃣ Auto-fix on Save (REAL productivity boost)

### VS Code Settings

```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  }
}
```

# 9️⃣ Interview-Level Understanding (VERY IMPORTANT)

### Common Interview Questions

**Q: Why both ESLint and Prettier?**
✔ ESLint prevents bugs
✔ Prettier ensures consistency

---

**Q: Can Prettier replace ESLint?**
❌ No — Prettier does not detect logic errors

---

**Q: Why disable ESLint formatting rules?**
✔ Single source of truth for formatting

---

**Q: What happens in CI if lint fails?**
✔ Build should fail → prevents bad code

---
