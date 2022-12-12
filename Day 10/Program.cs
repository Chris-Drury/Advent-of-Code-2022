namespace Day10
{
    class Problem
    {
        static private int clockCycle = 1;
        static private int xRegister = 1;
        static private int signalStrength = 0;

        static private List<List<string>> crtScreen = new List<List<string>>();

        static void Main(string[] args)
        {
            string[] instructionsInput = System.IO.File.ReadAllLines("input.txt");

            crtScreen.Add(new List<string>());
            drawSprite();

            foreach (string instruction in instructionsInput)
            {
                if (instruction.Contains("noop"))
                {
                    runNoOp();
                }
                else if (instruction.Contains("addx"))
                {
                    runAddX(int.Parse(instruction.Split()[1]));
                }
                checkClock();
            }

            Console.WriteLine($"Signal strength: {signalStrength}");

            printCrt();
        }

        static void runNoOp()
        {
            newCycle();
        }

        static void runAddX(int x)
        {
            newCycle();
            checkClock();

            xRegister += x;
            newCycle();
        }

        static void checkClock()
        {
            if((clockCycle - 20) % 40 == 0)
            {
                signalStrength += (xRegister * clockCycle);
            }
        }

        static void newCycle()
        {
            drawSprite();

            clockCycle++;
        }

        static bool ifSpriteOverlap(int sprite, int location)
        {
            return (((location % 40 - 1) == sprite) || (location % 40 == sprite) || ((location % 40 + 1) == sprite));
        }

        static void printCrt()
        {
            for (int i = 0; i < crtScreen.Count(); i++)
            {
                for (int j = 0; j < crtScreen[i].Count(); j++)
                {
                    Console.Write(crtScreen[i][j]);
                }
                Console.WriteLine();
            }
        }

        static void drawSprite()
        {
            if (clockCycle / 40 > (crtScreen.Count() - 1))
            {
                crtScreen.Add(new List<string>());
            }

            if (ifSpriteOverlap(xRegister, clockCycle))
            {
                crtScreen[clockCycle / 40].Add("#");
            }
            else
            {
                crtScreen[clockCycle / 40].Add(".");
            }
        }
    }
}