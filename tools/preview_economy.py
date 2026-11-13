"""Pure Python design preview. Not an in-game mod or LUA binding.

Use only for checking proposed formulas and example outcomes.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

CONFIG = Path(__file__).resolve().parents[1] / "config" / "balance_v0_1.json"


def estimate(
    max_soldiers: int,
    before_soldiers: int,
    replenished_soldiers: int,
    vanilla_upkeep: float,
    full_recruit_price: float,
    upkeep_multiplier: float = 0.5,
    replenishment_fraction: float = 1.0,
    scale_upkeep_with_strength: bool = True,
) -> dict[str, float]:
    """Estimate upkeep + fee for VERIFIED replenishment (not merges/new recruits)."""
    if max_soldiers <= 0:
        raise ValueError("max_soldiers must be > 0")
    if not (0 <= before_soldiers <= max_soldiers):
        raise ValueError("before_soldiers out of range")
    if not (0 <= replenished_soldiers <= max_soldiers - before_soldiers):
        raise ValueError("replenished_soldiers out of range")
    if min(vanilla_upkeep, full_recruit_price, upkeep_multiplier, replenishment_fraction) < 0:
        raise ValueError("Costs and multipliers cannot be negative")
    ratio = before_soldiers / max_soldiers if scale_upkeep_with_strength else 1.0
    maintenance = vanilla_upkeep * upkeep_multiplier * ratio
    replenish = full_recruit_price * replenishment_fraction * replenished_soldiers / max_soldiers
    return {
        "maintenance": round(maintenance, 2),
        "replenishment_fee": round(replenish, 2),
        "total": round(maintenance + replenish, 2),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview campaign economy formula (not a mod)")
    parser.add_argument("--max", type=int, default=120, dest="max_soldiers")
    parser.add_argument("--before", type=int, default=90)
    parser.add_argument("--replenished", type=int, default=20)
    parser.add_argument("--upkeep", type=float, default=200)
    parser.add_argument("--recruit", type=float, default=600)
    args = parser.parse_args()
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))["economy"]
    print(json.dumps(estimate(
        args.max_soldiers,
        args.before,
        args.replenished,
        args.upkeep,
        args.recruit,
        cfg["upkeep_multiplier"],
        cfg["replenishment_fee_fraction_of_full_recruit_price"],
        cfg["scale_upkeep_with_current_strength"],
    ), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
