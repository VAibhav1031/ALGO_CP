# Understanding Bit Manipulation 🔢

## What is Bit Manipulation? 

Bit manipulation involves working directly with bits - the 1s and 0s that make up all data in computing. We primarily use bitwise operators for this:

- AND - `&` (Ampersand)
- OR - `|` (Pipe)
- XOR - `^` (Caret)
- NOT - `~` (Tilde)

## Real-World Applications 🎮

Bit manipulation is more than just solving coding problems - it has practical applications:

### Board Games
When making board games, we often have large boards with values stored in arrays (matrices). Checking and computing every move can be redundant and slow down our game.

Instead, we can use bits to represent columns, rows, and other elements, updating and checking states using bitwise operators. This makes everything much faster!

### File Permissions (Unix/Linux) 📁

In Unix/Linux systems, file permissions are represented as "rwx" (read, write, execute) for User | Group | Everyone.

You've probably seen numbers like `755` associated with files. These represent permission sets:

- First digit (`7`) → User permissions
- Second digit (`5`) → Group permissions
- Third digit (`5`) → Everyone else's permissions

Each digit in binary represents the permission state:
- `7` in binary is `111` meaning read (1), write (1), execute (1) are all TRUE
- `5` in binary is `101` meaning read (1), write (0), execute (1)

Breaking down the permission values:
- Reading (leftmost/MSB): `100` in binary = `4` in decimal
- Writing (middle bit): `010` in binary = `2` in decimal
- Execution (rightmost/LSB): `001` in binary = `1` in decimal

## Still Exploring 🔍

I'm still exploring this topic myself, but it's amazing how bit manipulation makes complex operations simpler and more efficient!
