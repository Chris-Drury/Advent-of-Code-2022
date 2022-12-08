namespace Day8
{
    class Tree
    {
        public int height {get;}
        public bool visible {get; set;}

        public Tree(char heightChar, bool visible)
        {
            this.height = int.Parse(heightChar.ToString());
            this.visible = visible;
        }
    }
}