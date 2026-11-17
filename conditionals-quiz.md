# Conditionals & Boolean Logic: Agree or Disagree?

Evaluate each student's `if`-statement condition and decide whether you **agree** or **disagree** with their claim before expanding the answer.

Each question is shown twice: first in App Lab JavaScript (the code you write in class), then in AP exam pseudocode (the spelling used on the College Board reference sheet). The logic is the same in both.

---

### Warm-Up: Lunch Check
A student writes the following condition:
```java
if (!isHungry || hasFood)
```
AP exam pseudocode: `IF (NOT isHungry OR hasFood)`

They say this will check whether someone should eat lunch. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Disagree.**
- `!isHungry` checks if the person is **not** hungry.
- `||` (OR) evaluates to `true` if either side is true, meaning anyone who is not hungry will trigger the condition even when `hasFood` is `false`.
- **Fix:** `if (isHungry && hasFood)`
</details>

---

### Question 1: Weather Check
A student writes the following condition:
```java
if (!(isRaining || isSnowing))
```
AP exam pseudocode: `IF (NOT (isRaining OR isSnowing))`

They say this will check whether it is neither raining nor snowing. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Agree.**
- By **De Morgan's Law**, `!(isRaining || isSnowing)` is logically equivalent to `!isRaining && !isSnowing`. Both sides must be false for the condition to evaluate to `true`.
</details>

---

### Question 2: Login Security
A student writes the following condition:
```java
if (!hasPassword && hasBiometrics)
```
AP exam pseudocode: `IF ((NOT hasPassword) AND hasBiometrics)`

They say this will check whether a user lacks both a password and biometrics. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Disagree.**
- The `!` operator only applies to `hasPassword`, so this actually checks whether the user lacks a password **and has** biometrics.
- **Fix:** `if (!hasPassword && !hasBiometrics)`
</details>

---

### Question 3: Valid Score Range
A student writes the following condition:
```java
if (score >= 0 && score <= 100)
```
AP exam pseudocode: `IF (score ≥ 0 AND score ≤ 100)`

They say this will check whether `score` is a valid percentage between `0` and `100` inclusive. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Agree.**
- `&&` (AND) requires **both** sides to be true: the score must be at least `0` **and** at most `100`. A score of `150` fails the second test; a score of `-5` fails the first.
- The classic bug here is writing `||` instead — `score >= 0 || score <= 100` is `true` for **every** number, because any number passes at least one of the two tests.
</details>

---

### Question 4: Weekend Detector
A student writes the following condition:
```java
if (day == "Sat" || day == "Sun")
```
AP exam pseudocode: `IF (day = "Sat" OR day = "Sun")`

They say this will check whether `day` falls on a weekend. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Agree.**
- `||` (OR) requires only **one** side to be true, and a single `day` value only needs to match one of the two strings.
- The classic bug here is writing `&&` instead — one variable can never equal `"Sat"` and `"Sun"` at the same time, so that version would always be `false`.
</details>

---

### Question 5: Teenager Age Check
A student writes the following condition:
```java
if (age > 13 && age < 19)
```
AP exam pseudocode: `IF (age > 13 AND age < 19)`

They say this will check whether someone is a teenager (from age `13` through `19` inclusive). Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Disagree.**
- Strict inequalities (`>` and `<`) exclude the boundary values `age = 13` and `age = 19`, evaluating to `false` for both.
- **Fix:** `if (age >= 13 && age <= 19)`
</details>

---

### Question 6: Discount Eligibility
A student writes the following condition:
```java
if (!(isMember && hasCoupon))
```
AP exam pseudocode: `IF (NOT (isMember AND hasCoupon))`

They say this will check whether a shopper is neither a member nor has a coupon. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Disagree.**
- By **De Morgan's Law**, `!(isMember && hasCoupon)` distributes to `!isMember || !hasCoupon`, which checks whether the shopper lacks membership **or** lacks a coupon (it returns `true` even if they have one of the two).
- **Fix:** `if (!isMember && !hasCoupon)`
</details>

---

### Question 7: User Permissions
A student writes the following condition:
```java
if (isAdmin || isEditor && isActive)
```
AP exam pseudocode: `IF (isAdmin OR isEditor AND isActive)`

They say this will check whether a user is active and is either an admin or an editor. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Disagree.**
- `&&` has higher operator precedence than `||`, so this evaluates as `isAdmin || (isEditor && isActive)`. If `isAdmin = true`, `isEditor = false`, and `isActive = false`, the condition still evaluates to `true` for an inactive admin.
- **Fix:** `if ((isAdmin || isEditor) && isActive)`
</details>

---

### Question 8: Body Temperature Check
A student writes the following condition:
```java
if (!(temp != 98.6))
```
AP exam pseudocode: `IF (NOT (temp ≠ 98.6))`

They say this will check whether `temp` is equal to `98.6`. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Agree.**
- Negating `!=` (double negation) is logically identical to `if (temp == 98.6)`.
</details>

---

### Question 9: Ticket Status Filter
A student writes the following condition:
```java
if (status != "OPEN" || status != "PENDING")
```
AP exam pseudocode: `IF (status ≠ "OPEN" OR status ≠ "PENDING")`

They say this will check whether `status` is neither `"OPEN"` nor `"PENDING"`. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Disagree.**
- Any string is guaranteed to be not equal to at least one of those two values, so this condition is always `true` (even when `status` is `"OPEN"`).
- **Fix:** `if (status != "OPEN" && status != "PENDING")`
</details>

---

### Question 10: Low-Battery Warning
A student writes the following condition:
```java
if (isBatteryLow && !isPluggedIn)
```
AP exam pseudocode: `IF (isBatteryLow AND NOT isPluggedIn)`

They say this will check whether a laptop needs to display a low-battery warning while unplugged. Do you agree or disagree?

<details>
<summary><strong>Show Answer</strong></summary>

**Agree.**
- The warning should fire when the battery **is** low **and** the laptop is **not** plugged in. `isBatteryLow` supplies the first part and `!isPluggedIn` the second, and `&&` requires both.
- The classic bug here is putting the `!` on the wrong variable — `!isBatteryLow && isPluggedIn` checks almost the exact opposite situation.
</details>
