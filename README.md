# GIC Take Home Assignment

---

## Auto Driving Car Simulation Solution

This solution is designed to handle multiple scenarios:

### Scenario 1: Single Car Inside the Field Boundary

Given a field size of 10 x 10, when a single car is positioned within the field boundary
```text
Car 1: A, (1,2) N, FFRFFFFRRL
```
and the simulation is run, you will see the following message:
  ```text
  Your current list of cars are:
  - A, (1,2) N, FFRFFFFRRL
  ```

### Scenario 2: Two-Car Collision Within the Field Boundary

Given a field size of 10 x 10, when two cars are positioned within the field boundary
```text
Car 1: A, (1,2) N, FFRFFFFRRL
Car 2: B, (7,8) W, FFLFFFFFFF
```
and a collision occurs, you will see a message similar to the following:
```text
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
- B, (7,8) W, FFLFFFFFFF

After simulation, the result is:
- A, collides with B at (5,4) at step 7
- B, collides with A at (5,4) at step 7
```

### Scenario 3: Single Car Outside the Field Boundary

Given an initial field size of 4 x 4, attempting to position a car outside the field boundary
```text
Car 1: A, (4,2) W, FFRFFFFRRL
```
will result in the following warning:
```text
Car A initial position is out of bounds.
```

### Scenario 4: Three Cars with an Initial Collision

With an initial field size of 7 x 7, three cars are positioned within the field boundary, 
```text
Car 1: A, (3,1) E, FFLFLFLFFF
Car 2: B, (2,4) S, FLFFLFFRFF
Car 3: C, (6,2) W, FLFRFFRFFL
```
and a collision occurs involving two of them. You will see the following message:
```text
Your current list of cars are:
- A, (3,1) E, FFLFLFLFFF
- B, (2,4) S, FLFFLFFRFF
- C, (6,2) W, FLFRFFRFFL

After simulation, the result is:
- A, collides with C at (5,1) at step 3
- C, collides with A at (5,1) at step 3
- B, (6,5) E
```

### Scenario 5: Three Cars with Sequential Collisions

In a 7 x 7 field, three cars are positioned within the boundary. Initially, two cars collide, followed by the third car colliding with the others at a much later step. You will see the following message:

The first two scenarios follow the assignment instructions. Additionally, I have included three extra scenarios to effectively address corner cases.

---

## How to Run the Test Scenarios:

To execute the test scenarios, use the following command:

```bash
python -m unittest
```