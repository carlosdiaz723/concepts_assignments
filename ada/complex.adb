with Ada.Exceptions;
use Ada.Exceptions;

-- Carlos Diaz
-- Source for Ada Assignment

package body Complex is

  function "*" (C1, C2: in Complex) return Complex is
    C: Complex := Create_Complex (R => (C1.Real * C2.Real) - (C1.Imag * C2.Imag), I => (C1.Real * C2.Imag) + (C1.Imag * C2.Real));
    begin
      return C;
    end "*";
    
    --------------------------------------------------------------------------------------------------------

  function "+" (C1, C2: in Complex) return Complex is
    C: Complex := Create_Complex (R => C1.Real + C2.Real, I => C1.Imag + C2.Imag);
    begin
      return C;
    end "+";
    
    ---------------------------------------------------------------------------------------------------------

  function "-" (C1, C2: in Complex) return Complex is
    C: Complex := Create_Complex (R => C1.Real - C2.Real, I => C1.Imag - C2.Imag);
    begin
      return C;
    end "-";

    -----------------------------------------------------------------------------------------------------------

  function "/" (C1, C2: in Complex) return Complex is
    Left : Float := (C1.Real * C2.Real) + (C1.Imag * C2.Imag);
    Right : Float := (C1.Imag * C2.Real) - (C1.Real * C2.Imag);
    Bottom : Float := (C2.Real * C2.Real) + (C2.Imag * C2.Imag);
    RealHalf : Float := Left / Bottom;
    ImagHalf : Float := Right / Bottom;
    C: Complex := Create_Complex (R => RealHalf, I => ImagHalf);
    begin
      return C;
    end "/";

    ------------------------------------------------------------------------------------------------------------------

  function Create_Complex (R: in Float; I: in Float) return Complex is
    C: Complex;
    begin
      C.Real := R;
      C.Imag := I;
      return C;
    end Create_Complex;

    --------------------------------------------------------------------------------------------------------------------

  function get_real (C: in Complex) return Float is
    begin
      return C.Real;
    end get_real;

    ---------------------------------------------------------------------------------------------------------------------

  function get_imag (C: in Complex) return Float is

    begin
      return C.Imag;
    end get_imag;

    ----------------------------------------------------------------------------------------------------------------------
end Complex;

