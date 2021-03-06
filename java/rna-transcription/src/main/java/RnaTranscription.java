class RnaTranscription
{

    String transcribe(String dnaStrand)
    {
      int len = dnaStrand.length();
      String rnaStrand = "";

      for (int i=0; i < len; i++)
      {
        switch (dnaStrand.charAt(i))
        {
          case 'G':
            rnaStrand += "C";
            break;
          case 'C':
            rnaStrand += "G";
            break;
          case 'T':
            rnaStrand += "A";
            break;
          case 'A':
            rnaStrand += "U";
            break;
          default:
            throw new IllegalArgumentException("Invalid input");
        }
      }
      return rnaStrand;
    }
}
