
--Base mod add
--underground transport belt
require("prototypes.base-mod.entity.transport-belt")
require("prototypes.base-mod.recipes.transport-belt")
require("prototypes.base-mod.technology.transport-belt")
require("prototypes.base-mod.items.transport-belt")
--underground pipes
require("prototypes.base-mod.entity.pipe")
require("prototypes.base-mod.recipes.pipe")
require("prototypes.base-mod.technology.pipe")
require("prototypes.base-mod.items.pipe")
--electric poles
require("prototypes.base-mod.entity.electric-pole")
require("prototypes.base-mod.recipes.electric-pole")
require("prototypes.base-mod.items.electric-pole")
require("prototypes.base-mod.technology.electric-pole")



data:extend({
    {
        type = "item-subgroup",
        name = "belt-to-ground",
        group = "logistics",
        order = "b",
    },
	{
        type = "item-subgroup",
        name = "pipe-to-ground",
        group = "logistics",
        order = "d",
    }
})
data.raw.recipe["basic-transport-belt-to-ground"].subgroup = "belt-to-ground"
data.raw.recipe["basic-transport-belt-to-ground"].order = "a[basic-transport-belt-to-ground]-a[basic-transport-belt-to-ground]"
data.raw.recipe["fast-transport-belt-to-ground"].subgroup = "belt-to-ground"
data.raw.recipe["fast-transport-belt-to-ground"].order = "b[fast-transport-belt-to-ground]-a[fast-transport-belt-to-ground]"
data.raw.recipe["express-transport-belt-to-ground"].subgroup = "belt-to-ground"
data.raw.recipe["express-transport-belt-to-ground"].order = "c[express-transport-belt-to-ground]-a[express-transport-belt-to-ground]"
data.raw.recipe["pipe-to-ground"].subgroup = "pipe-to-ground"
data.raw.recipe["pipe-to-ground"].order = "a[pipe-to-ground]-a[pipe-to-ground]"
data.raw.recipe["medium-pipe-to-ground"].subgroup = "pipe-to-ground"
data.raw.recipe["medium-pipe-to-ground"].order = "b[medium-pipe-to-ground]-b[medium-pipe-to-ground]"
data.raw.recipe["long-pipe-to-ground"].subgroup = "pipe-to-ground"
data.raw.recipe["long-pipe-to-ground"].order = "c[long-pipe-to-ground]-c[long-pipe-to-ground]"
data.raw.recipe["ultra-pipe-to-ground"].subgroup = "pipe-to-ground"
data.raw.recipe["ultra-pipe-to-ground"].order = "d[ultra-pipe-to-ground]-d[ultra-pipe-to-ground]"
data.raw.recipe["continental-pipe-to-ground"].subgroup = "pipe-to-ground"
data.raw.recipe["continental-pipe-to-ground"].order = "e[continental-pipe-to-ground]-e[continental-pipe-to-ground]"
