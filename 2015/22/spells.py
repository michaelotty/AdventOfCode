"""Spell related classes"""

from dataclasses import dataclass


@dataclass(kw_only=True)
class Effect:
    """Effect class"""

    turns = 1
    armor = 0
    damage = 0
    mana_boost = 0


@dataclass(kw_only=True)
class Spell:
    """Spell class"""

    mana = 10
    damage = 0
    healing = 0
    effect = Effect()


# def create_spell(self, spell_name: str) -> Spell:
#     """Spell creator"""
#     spells = {
#         "magic_missile": Spell(mana=53, damage=4),
#         "drain": Spell(mana=73, damage=2, healing=2),
#         "shield": Spell(mana=113, effect=Effect(turns=6, armor=7)),
#         "poison": Spell(mana=173, effect=Effect(turns=6, damage=3)),
#         "recharge": Spell(mana=229, effect=Effect(turns=5, mana_boost=101)),
#     }
#     return spells[spell_name]
