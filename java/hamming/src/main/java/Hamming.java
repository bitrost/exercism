public class Hamming
{
  private int hammingDistance;

  Hamming(String leftStrand, String rightStrand)
  {
    hammingDistance = findHammingDistance(leftStrand, rightStrand);
  }

  int findHammingDistance(String leftStrand, String rightStrand)
  {
    int counter = 0;

    if (leftStrand.length() == rightStrand.length())
    {
      for (int i = 0; i < leftStrand.length(); i++)
      {
        if (leftStrand.charAt(i) != rightStrand.charAt(i))
        {
          counter++;
        }
      }
    }
    else
    {
      throw new IllegalArgumentException("leftStrand and rightStrand must be of equal length.");
    }

    return counter;
  }

  int getHammingDistance()
  {
    return hammingDistance;
  }
}
