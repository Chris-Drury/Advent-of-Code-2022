namespace Day8
{
    class Tree
    {
        internal int height {get;}
        internal bool visible {get; set;}

        public Tree(char heightChar, bool visible)
        {
            this.height = int.Parse(heightChar.ToString());
            this.visible = visible;
        }
    }
}