Problem
Description

Implement
a
Last
In
First
Out(LIFO)
stack
using
queues
only.

The
implemented
stack
should
support
all
the
basic
functions
of
a
normal
stack(push, top, pop, and empty).

Implement
the
UserStack


class:


void
push(int
X): Pushes
element
X
to
the
top
of
the
stack.
int
pop(): Removes
the
element
on
the
top
of
the
stack and returns
it.
int
top(): Returns
the
element
on
the
top
of
the
stack.
boolean
empty(): Returns
true if the
stack is empty, false
otherwise.
NOTE:

You
must
use
only
standard
operations
of
a
queue, which
means
only
push
to
back, peek / pop
from front, size, and is empty
operations
are
valid.
Depending
on
your
language, the
queue
may
not be
supported
natively.You
may
simulate
a
queue
using
a
list or deque(double - ended
queue), as long as you
use
only
a
queue
's standard operations.

Problem
Constraints

1 <= X <= 109

At
most
1000
calls
will
be
made
to
push, pop, top, and empty
function.

All
the
calls
to
pop and top
are
valid.i.e.pop and top
are
called
only
when
the
stack is non - empty.

Example
Input

Input
1:

1) UserStack()
2) push(20)
3) empty()
4) top()
5) pop()
6) empty()
7) push(30)
8) top()
9) push(40)
10) top()
Input
2:

1) UserStack()
2) push(10)
3) push(20)
4) push(30)
5) pop()
6) pop()

Example
Output

Output 1:

false

20
20

true

30

40

Output 2:

30
20

Example

Explanation

Explanation 1:
    
      |  |      |  |      |  |      |  |
      |  | ---> |  | ---> |  | ---> |40|
      |20|      |  |      |30|      |30|
      |__|      |__|      |__|      |__|

Explanation 2:

      |  |      |  |      |30|      |  |      |  |
      |  | ---> |20| ---> |20| ---> |20| ---> |  |
      |10|      |10|      |10|      |10|      |10|
      |__|      |__|      |__|      |__|      |__|

