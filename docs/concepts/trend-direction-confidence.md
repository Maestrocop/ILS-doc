# Trend Direction & Confidence

Trend analysis in ILS combines two related facts:
- whether mastery is moving up or down, and
- how confident the system is that the movement is real.

## Trend direction

- **Up** means the latest mastery score is higher than the previous snapshot.
- **Down** means the latest mastery score is lower.
- **Flat** means the score has not changed significantly between the last two snapshots.
- **No trend** means there is only one snapshot and the system cannot determine a direction yet.

> Important: “Flat” or “Stable” is a directional signal, not a score judgment. A student can be flat at 3.3 and still be below the target threshold.

## Trend confidence

Trend confidence measures how dependable the direction signal is.

- **High** confidence: multiple consistent snapshots and clear score movement.
- **Medium** confidence: enough history exists, but the change is smaller or less consistent.
- **Low** confidence: limited snapshot history or mixed score signals.
- **Insufficient**: too few snapshots to compute a reliable trend.

## Why both matter

- Direction alone can be noisy: a single low score can look like a downward trend.
- Confidence helps teachers interpret whether the direction is stable or temporary.

## Example

- A student moves from 6.5 to 7.4, with a prior sequence of rising scores: direction is Up, confidence is High.
- A student moves from 8.0 to 7.8 after only one prior snapshot: direction is Down, confidence is Low.


**Last updated:** 2026-07-08
