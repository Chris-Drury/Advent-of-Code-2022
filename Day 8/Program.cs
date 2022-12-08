namespace Day8
{
    class Problem
    {
        private static int forestSize;
        static void Main(string[] args)
        {
            string[] forestInput = System.IO.File.ReadAllLines("input.txt");

            List<List<Tree>> forest = new List<List<Tree>>();

            foreach (string forestLine in forestInput)
            {
                List<Tree> treeList = new List<Tree>();

                foreach (char charTree in forestLine)
                {
                    treeList.Add(new Tree(charTree, false));
                }

                forest.Add(treeList);
            }

            forestSize = forest.Count();

            checkVisibilityByColumns(forest, false);
            checkVisibilityByColumns(forest, true);

            forest = transposeForest(forest);

            checkVisibilityByColumns(forest, false);
            checkVisibilityByColumns(forest, true);

            Console.WriteLine($"Number of visible trees: {countTotalVisible(forest)}");

            Part2.nextPart(forest);
        }

        public static List<List<Tree>> transposeForest(List<List<Tree>> forest)
        {
            List<List<Tree>> transposedForest = new List<List<Tree>>();
        
            for (int column = 0; column < forestSize; column++)
            {
                transposedForest.Add(new List<Tree>());

                for (int row = 0; row < forestSize; row++)
                {
                    transposedForest[column].Add(forest[row][column]);
                }
            }

            return transposedForest;
        }

        private static void checkVisibilityByColumns(List<List<Tree>> forest, bool upwards)
        {
            for (int row_index = 0; row_index < forestSize; row_index++)
            {
                int row = upwards ? forestSize - row_index - 1 : row_index;
                int tallestTree = -1;

                for (int column_index = 0; column_index < forestSize; column_index++)
                {
                    int column = upwards ? forestSize - column_index - 1 : column_index;

                    Tree tree = forest[column][row];
                    int treeHeight = tree.height;

                    if (treeHeight > tallestTree)
                    {
                        tree.visible = true;
                        tallestTree = treeHeight;
                    }
                }
            }
        }

        private static int countTotalVisible(List<List<Tree>> forest)
        {
            int totalVisible = 0;

            for (int column = 0; column < forestSize; column++)
            {
                for (int row = 0; row < forestSize; row++)
                {
                    if (forest[row][column].visible == true)
                    {
                        totalVisible++;
                    }
                }
            }
            return totalVisible;
        }
    }
}
