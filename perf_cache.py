"""Small utilities demonstrating a high-impact, low-effort performance win.

The code here focuses on memoizing expensive repeated computations so the same
inputs return instantly after the first pass.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def memoize(func: F) -> F:
    """Cache results by argument tuple to avoid repeated expensive work.

    This is the single best low-effort optimization when a function is called many
    times with the same inputs. It turns repeated O(n) work into amortized O(1)
    after the initial computation.
    """
    cache: Dict[tuple[Any, ...], Any] = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return cast(F, wrapper)


@memoize
def fibonacci(n: int) -> int:
    """Compute Fibonacci numbers without re-evaluating identical inputs."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
