data:extend(
{
 {
    type = "recipe",
    name = "medium-basic-transport-belt-to-ground",
    enabled = "false",
    energy_required = 1,
    ingredients =
    {
        {"iron-plate", 30},
        {"basic-transport-belt", 15}
    },
    result_count = 2,
    result = "medium-basic-transport-belt-to-ground"
  },
   {
    type = "recipe",
    name = "long-basic-transport-belt-to-ground",
    enabled = "false",
    energy_required = 1,
    ingredients =
    {
      {"steel-plate", 30},
      {"basic-transport-belt", 30}
    },
    result_count = 2,
    result = "long-basic-transport-belt-to-ground"
  },
  {
    type = "recipe",
    name = "medium-fast-transport-belt-to-ground",
    enabled = "false",
    ingredients =
    {
      {"iron-gear-wheel", 40},
      {"medium-basic-transport-belt-to-ground", 2}
    },
    result_count = 2,
    result = "medium-fast-transport-belt-to-ground"
  },
  {
    type = "recipe",
    name = "long-fast-transport-belt-to-ground",
    enabled = "false",
    ingredients =
    {
      {"iron-gear-wheel", 80},
      {"long-basic-transport-belt-to-ground", 2}
    },
    result_count = 2,
    result = "long-fast-transport-belt-to-ground"
  },
  {
    type = "recipe",
    name = "medium-express-transport-belt-to-ground",
    enabled = "false",
    ingredients =
    {
        {"iron-gear-wheel", 80},
        {"medium-fast-transport-belt-to-ground", 2}
    },
    result_count = 2,
    result = "medium-express-transport-belt-to-ground"
  },
   {
    type = "recipe",
    name = "long-express-transport-belt-to-ground",
    enabled = "false",
    ingredients =
    {
        {"iron-gear-wheel", 160},
        {"long-fast-transport-belt-to-ground", 2}
    },
    result_count = 2,
    result = "long-express-transport-belt-to-ground"
  } 
  }
  )