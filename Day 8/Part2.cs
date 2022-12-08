namespace Day8
{
    class Part2
    {
        private static int forestSize;
        public static void nextPart(List<List<Tree>> forest)
        {
            forestSize = forest.Count();
            int bestScenicScore = 0;

            for (int column = 0; column < forestSize; column++)
            {
                for (int row = 0; row < forestSize; row++)
                {
                    int scenicScore = determineScenicScore(forest, row, column);

                    if (scenicScore > bestScenicScore)
                    {
                        bestScenicScore = scenicScore;
                    }
                }
            }

            Console.WriteLine("Best Scenic Score: " + bestScenicScore);
        }

        private static int determineScenicScore(List<List<Tree>> forest, int row, int column)
        {
            int westScenic = scoreTreeScenery(forest, row, column, true);   
            int eastScenic = scoreTreeScenery(forest, row, column, false);   

            forest = Problem.transposeForest(forest);

            int northScenic = scoreTreeScenery(forest, column, row, true);   
            int southScenic = scoreTreeScenery(forest, column, row, false);   

            return northScenic * southScenic * eastScenic * westScenic;
        }

        private static int scoreTreeScenery(List<List<Tree>> forest, int row, int column, bool upwards)
        {
            int treeHeight = forest[row][column].height;

            int directionalSceneryScore = 0;

            column = upwards ? column - 1 : column + 1;
            while (column >= 0 && (column < forestSize))
            {
                int nextTreeHeight = forest[row][column].height;

                directionalSceneryScore++;
                if (nextTreeHeight >= treeHeight)
                {
                    break;
                }

                column = upwards ? column - 1 : column + 1;
            }

            return directionalSceneryScore;
        }
    }
}