namespace Day9
{
    class BridgePoint
    {
        internal int x {get; set;}
        internal int y {get; set;}

        public BridgePoint(int x, int y)
        {
            this.x = x;
            this.y = y;
        }

        public void moveRight()
        {
            x++;
        }

        public void moveLeft()
        {
            x--;
        }

        public void moveUp()
        {
            y++;
        }

        public void moveDown()
        {
            y--;
        }

        public override bool Equals(Object obj)
        {
            return (obj is BridgePoint) && 
                ((BridgePoint)obj).x == x && 
                ((BridgePoint)obj).y == y;
        }
    }
}