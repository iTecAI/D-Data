# Specification

## Spells
### Targets

- `specific` - Indicates a number of specific targets
  - `count` - (int)/"string" (required) Number of targets, or "any".
- `area` - Indicates that the targets should be within an area
  - `area` - (int) (required) Area width/diameter in feet
  - `area_type` - "string" (required) `sphere`, `cube`, `line`, `cone`, `cylinder`
- `prerequisites` - Indicates that the spell has prerequisites
  - `prerequisites` - {dict} (required) Prerequisite definitions
    - `{prerequisite name}` - {dict} (required at least 1)
      - `operator` - "string" (required) Comparison operator (`==`,`<=`,`>=`,`<`,`>`,`!=`) to apply to the `value`
      - `value` - (any) (required) Value to check
  - `prerequisites_match` - "string" (required) Either of `all`, `any`. Indicates whether the target must match all or any of the prerequisites.
- `slot_scale` - Indicates that the spell scales with higher slot levels
  - `slot_scale` - [list] (required)
    - Item - {dict} (required at least 1)
      - `path` - "string" (required) Path to value to append the value to.
      - `value` - (any) (required) Value to add.

### Effects
- `spell_attack` - Indicates a spell attack
- `failure_effect` - Indicates some effect will occur on a miss/successful save
  - `fail` - [list] (required) List of **Effects**.
- `damage` - Indicates that the effect will deal damage on a hit/failed save
  - `damage` - {dict} (required)
    - `roll` - "roll string" (required) Roll string
    - `type` - "string" (required) Damage type
    - `recurring` - {dict} (optional) Include if damage continues after the first dealing
      - `roll` - "roll string" (required) Roll string
      - `type` - "string" (required) Damage type
      - `rounds` - (int) (required) Number of rounds to recur for
      - `turn` - "string" (required) Whether to damage on the `start` or `end` of the turn
- `save` - Indicates that a save must be made
  - `save` - "string" (required) Save name, such as `strength` or `dexterity`
- `cantrip_scaling` - Indicates that the spell will change as the player levels.
  - `{level number}` - {dict} (required at least 1)
    - `target` - "string" (required) Path inside the effect dict, such that damage:{roll:-} -> `damage.roll`
    - `value` - (any) (required) Value to set the target path item to.
- `required` - Indicates that an effect will occur if its prerequisites are met, and will not appear as an optional effect. If only one optional effect is available, it will activate automatically.
- `attribute` - Indicates that the effect will be changing an attribute on the target
  - `attributes` - [list] (required) List of **Attributes**
    - **Attribute** - {dict} (required at least 1)
      - `path` - "string" (required) Path to attribute on target
      - `operation` - "string" (required) Any of `add`, `subtract`, `multiply`, `divide`, `set`
      - `value` - "roll string" (required) Value to use with operator on attribute
- `condition` - Indicates that the effect applies a condition to the target
  - `condition` - "string" (required) Condition to apply to the target. Duration is assumed to be that of the spell.
- `flavor` - Indicates that the effect will output flavor text on a success
  - `flavor` - "string" (required) Flavor text to output/report
- `roll_modifier` - Indicates that the effect will modify the target's rolls on a success
  - `modifier` - {dict} (required)
    - `roll` - "roll string" (required) Roll string to add to the target's rolls.
    - `affected` - [list] (required at least one) List of rolls to affect. May be `attacks`, `saves`, or `checks`. May also be more specific for `saves` and `checks`, such as `checks.stealth` or `saves.intelligence`
- `slot_scale` - Indicates that the spell scales with higher slot levels
  - `slot_scale` - [list] (required)
    - Item - {dict} (required at least 1)
      - `path` - "string" (required) Path to value to append the value to.
      - `value` - (any) (required) Value to add.