# Performance improvement list

1. Memoize repeated expensive calculations.
2. Replace nested loops with set or dict lookups when possible.
3. Batch database calls and reduce round-trips.
4. Avoid converting large data structures multiple times.
5. Cache HTTP responses for stable inputs.
6. Stream large files instead of loading them into memory all at once.
7. Delay work until it is actually needed (lazy evaluation).
8. Reuse objects and buffers instead of reallocating them in hot loops.
9. Offload CPU-heavy work to worker processes or async tasks when independent.
10. Profile before optimizing to focus on real bottlenecks.

## Highest-impact, lowest-effort win

Memoization is the most practical optimization in the short term because it has a high payoff and very little code churn. It turns repeated work into a single computation per unique input, which often reduces latency dramatically for hot code paths.

This repo includes a simple Python example in `perf_cache.py` that demonstrates the pattern.
