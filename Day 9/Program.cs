namespace Day9
{
    class Problem
    {
        static private List<BridgePoint> tailLocations = new List<BridgePoint>();
        static private List<BridgePoint> finalTailLocations = new List<BridgePoint>();
        static private int tailCount = 9;

        static void Main(string[] args)
        { 
            // Initialize for 9 points
            for (int i = 0; i < tailCount; i++)
            {
                tailLocations.Add(new BridgePoint(0,0));
            }


            string[] movementInput = System.IO.File.ReadAllLines("input.txt");

            applyMovements(movementInput);

            int totalUniqueLocations = countUniqueLocations();

            Console.WriteLine($"Unique locations visited: {totalUniqueLocations}");
        }

        private static void applyMovements(string[] movements)
        {
            BridgePoint headLocation = new BridgePoint(0,0);
            finalTailLocations.Add(new BridgePoint(0,0));

            foreach (string movement in movements)
            {
                string[] movementCommands = movement.Split();

                string direction = movementCommands[0];
                int amount = int.Parse(movementCommands[1]);

                for (int moved = 0; moved < amount; moved++)
                {
                    switch(direction)
                    {
                        case "U":
                            headLocation.y++;
                            break;
                        case "R":
                            headLocation.x++;
                            break;
                        case "D":
                            headLocation.y--;
                            break;
                        case "L":
                            headLocation.x--;
                            break;
                        default:
                            Console.WriteLine($"Unknown direction symbol: {direction}. returning...");
                            return;
                    }

                    tailLocations[0] = new BridgePoint(headLocation.x, headLocation.y);

                    for (int tailIndex = 0; tailIndex < tailCount; tailIndex++)
                    {
                        bool lastTail = ((tailIndex + 1) == tailCount);
                        BridgePoint currentTailPoint;

                        if(!lastTail)
                        {
                            currentTailPoint = tailLocations[tailIndex + 1];
                        }
                        else
                        {
                            currentTailPoint = finalTailLocations.Last();
                        }

                        moveTail(tailLocations[tailIndex], tailIndex, lastTail);
                    }
                }
            }
        }

        private static void moveTail(BridgePoint headLocation, int tailIndex, bool lastTail)
        {
            BridgePoint currentTailPoint;

            if(!lastTail)
            {
                currentTailPoint = tailLocations[tailIndex + 1];
            }
            else
            {
                currentTailPoint = finalTailLocations.Last();
            }

            int xDifference = headLocation.x - currentTailPoint.x;
            int yDifference = headLocation.y - currentTailPoint.y;

            // Is adjacent ? leave where it is : move with head
            if ((Math.Abs(xDifference) <= 1) && (Math.Abs(yDifference) <= 1))
            {
                return;
            }

            if (moveInDirectLine(true, currentTailPoint, xDifference, yDifference, lastTail, tailIndex)) return;
            if (moveInDirectLine(false, currentTailPoint, xDifference, yDifference, lastTail, tailIndex)) return;

            int xToMove = (xDifference > 1) ? 1 : (xDifference < -1) ? -1 : xDifference;
            int yToMove = (yDifference > 1) ? 1 : (yDifference < -1) ? -1 : yDifference;

            // Move diagonally
            if (!lastTail)
            {
                tailLocations[tailIndex + 1] = new BridgePoint(currentTailPoint.x + xToMove, currentTailPoint.y + yToMove);
            }
            else
            {
                finalTailLocations.Add(new BridgePoint(currentTailPoint.x + xToMove, currentTailPoint.y + yToMove));
            }

            
            return;
        }

        private static bool moveInDirectLine(bool isX, BridgePoint currentTailPoint, int xDifference, int yDifference, bool lastTail, int tailIndex)
        {
            if((isX && (Math.Abs(xDifference) == 2) && (Math.Abs(yDifference) == 0)) 
                || (!isX && (Math.Abs(xDifference) == 0) && (Math.Abs(yDifference) == 2)))
            {
                BridgePoint newTailPoint = new BridgePoint(currentTailPoint.x, currentTailPoint.y);
                
                if (isX)
                {
                    if (xDifference > 0)
                    {
                        newTailPoint.moveRight();
                    }
                    else 
                    {
                        newTailPoint.moveLeft();
                    }
                }
                else
                {
                    if (yDifference > 0)
                    {
                        newTailPoint.moveUp();
                    }
                    else 
                    {
                        newTailPoint.moveDown();
                    }
                }

                if (!lastTail)
                {
                    tailLocations[tailIndex + 1] = newTailPoint;
                }
                else
                {
                    finalTailLocations.Add(newTailPoint);
                }

                return true;
            }

            return false;
        }

        private static int countUniqueLocations()
        {
            List<BridgePoint> uniqueLocations = new List<BridgePoint>();

            foreach (BridgePoint location in finalTailLocations)
            {
                Console.WriteLine($"{location.x}, {location.y}");

                if(!uniqueLocations.Contains(location))
                {
                    uniqueLocations.Add(location);
                }

            }

            return uniqueLocations.Count();
        }
    }
}
