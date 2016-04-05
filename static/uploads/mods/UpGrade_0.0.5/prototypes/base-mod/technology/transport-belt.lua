data:extend(
{
{
    type = "technology",
    name = "logistics-upgrade-1",
    icon = "__base__/graphics/icons/basic-transport-belt-to-ground.png",
    effects =
    {
      {
        type = "unlock-recipe",
        recipe = "medium-basic-transport-belt-to-ground"
      }
    },
    prerequisites = {"logistics"},
    unit =
    {
      count = 40,
      ingredients =
      {
        {"science-pack-1", 1}
      },
      time = 15
    },
    order = "a-f-b",
  },
  {
    type = "technology",
    name = "logistics-upgrade-2",
    icon = "__base__/graphics/icons/basic-transport-belt-to-ground.png",
    effects =
    {
      {
        type = "unlock-recipe",
        recipe = "long-basic-transport-belt-to-ground"
      }
    },
    prerequisites = {"logistics", "logistics-upgrade-1"},
    unit =
    {
      count = 80,
      ingredients =
      {
        {"science-pack-1", 1},
		{"science-pack-2", 1}
      },
      time = 30
    },
    order = "a-f-b",
  },
  {
    type = "technology",
    name = "logistics-2-upgrade-1",
    icon = "__base__/graphics/icons/fast-transport-belt-to-ground.png",
    effects =
    {
      {
        type = "unlock-recipe",
        recipe = "medium-fast-transport-belt-to-ground"
      }
    },
    prerequisites = {"logistics-2", "logistics-upgrade-1"},
    unit =
    {
      count = 40,
      ingredients =
      {
        {"science-pack-1", 1},
		{"science-pack-2", 1}
      },
      time = 15
    },
    order = "a-f-b",
  },
  {
    type = "technology",
    name = "logistics-2-upgrade-2",
    icon = "__base__/graphics/icons/fast-transport-belt-to-ground.png",
    effects =
    {
      {
        type = "unlock-recipe",
        recipe = "long-fast-transport-belt-to-ground"
      }
    },
    prerequisites = {"logistics-2", "logistics-2-upgrade-1", "logistics-upgrade-2"},
    unit =
    {
      count = 80,
      ingredients =
      {
        {"science-pack-1", 1},
		{"science-pack-2", 1},
		{"science-pack-3", 1}
      },
      time = 30
    },
    order = "a-f-b",
  },
  {
    type = "technology",
    name = "logistics-3-upgrade-1",
    icon = "__base__/graphics/icons/express-transport-belt-to-ground.png",
    effects =
    {
      {
        type = "unlock-recipe",
        recipe = "medium-express-transport-belt-to-ground"
      }
    },
    prerequisites = {"logistics-3", "logistics-2-upgrade-1"},
    unit =
    {
      count = 40,
      ingredients =
      {
        {"science-pack-1", 1},
		{"science-pack-2", 1},
		{"science-pack-3", 1}
      },
      time = 15
    },
    order = "a-f-b",
  },
  {
    type = "technology",
    name = "logistics-3-upgrade-2",
    icon = "__base__/graphics/icons/express-transport-belt-to-ground.png",
    effects =
    {
      {
        type = "unlock-recipe",
        recipe = "long-express-transport-belt-to-ground"
      }
    },
    prerequisites = {"logistics-3", "logistics-3-upgrade-1"},
    unit =
    {
      count = 80,
      ingredients =
      {
        {"science-pack-1", 1},
		{"science-pack-2", 1},
		{"science-pack-3", 1}
      },
      time = 30
    },
    order = "a-f-b",
  }
  }
  )