import BeautifulSoup
import requests

sampletext = """
recipe: Brownie Layer:

4 oz unsalted butter

3 oz unsweeted chocolate

1 cup all purpose flour

1/4 tsp baking powder

1/4 tsp salt

3 eggs

1 cup sugar

1 tsp grated orange zest

1/4 tsp orange extract

1/4 tsp vanilla extract

Melt the butter and chocolate over a double boiler. Preheat oven to 325 degrees F. Brush a 9x13 inch pan with butter. Sift flour, baking powder and salt together. Mix the eggs, sugar, zest and extracts together in a separate bowl. Stir the egg mixture into the chocolate butter. Add the dry ingredients and mix well. Spread batter into prepared pan. Bake 25-30 minutes until set, but not dry. Cool about 10 minutes.

Orange Layer:

1 3/4 cup sugar

1/4 cup all purpose flour

1/2 tsp baking powder

4 tsp grated orange zest

1/2 cup fresh squeezed orange juice

1/4 cup fresh squeezed lemon juice

1 tsp orange flower water, optional

1/2 tsp orange extract

4 eggs

Sift the sugar, flour, and baking powder into a large bowl. Whisk in the orange zest, both juices, flower water if using, and extract. Whisk in the eggs, stirring until smooth. Pour over the pre-baked brownie and bake another 45-50 minutes, until the filling puffs up. The top should be golden brown and the filling set. Cool completely. Refrigerate until cold before cutting. Wipe your knife clean between each cut. To serve, dust with powdered sugar.

Yield: 24, 2 inch square bars
"""

def main():
    # todo instantiate reddit API
    # scroll through unsaved new posts in list of subreddits
    # parse OP and comments for recipes..? - look for "Ingredients", "Recipe", measurements?
    # convert here
    # post back as a comment, save post to avoid repeats

    # think of a good way to get feedback?

    response = requests.post('https://convertrecipe.com/convert_US_to_metric.php', data=dict(recipe=sampletext))
    soup = BeautifulSoup.BeautifulSoup(response.text)
    metric_recipe = soup.find("textarea", {"id": "recipe_in_metric"})

    metric_recipe_text = metric_recipe.contents
    print(metric_recipe_text)

if __name__ == "__main__":
    main()