import java.util.ArrayList;

public class PangramChecker
{

    public static boolean isPangram(String input)
    {
      ArrayList<String> letters = new ArrayList<String>();
      char current;

      input = input.toLowerCase();

      // Adds letters of alphabet to ArrayList
      for (char ch = 'a'; ch <= 'z'; ch++)
      {
        letters.add(String.valueOf(ch));
      }

      for (int i = 0; i < input.length(); i++)
      {
        current = input.charAt(i);
        if (!letters.contains(current))
        {
          letters.remove(Character.toString(current));
        }
      }

      if (letters.isEmpty())
      {
        return true;
      }
      else
      {
        return false;
      }
    }
}
