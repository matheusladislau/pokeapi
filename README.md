# pokeapi

To download pokemon info (json)
1. execute producer/get_pokemon.py to download info of all pokemon to folder /data/pokemon with pattern pokemon_<id>.json
1.1 execute producer/merge_pokemon.py to merge all pokemon data

To download assets
1.2 execute producer/get_pokemon_sprites to donwload all cries(.ogg) and sprites(.png and .svg) to folder data/cries and data/sprites

To download types info (json)
2. execute producer/get_types.py to download info of all types to folder /data/types with pattern <type name>.json
2.1 execute producer/merge_types.py to merge all types data
