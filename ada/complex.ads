package Complex is

  type Complex is private;
  
  -- Carlos Diaz
  -- Source for Ada Assignment

  function Create_Complex (R: in Float; I: in Float) return Complex;
  -- pre: none
  -- post: complex number with real part R & imaginary part I has been created
  
  function "+" (C1, C2: in Complex) return Complex;
  -- pre: none
  -- post: sum of C1 & C2 is returned
  
  function "-" (C1, C2: in Complex) return Complex;
  -- pre: none
  -- post: difference of C1 & C2 is returned
  
  function "*" (C1, C2: in Complex) return Complex;
  -- pre: none
  -- post: product of C1 & C2 is returned
  
  function "/" (C1, C2: in Complex) return Complex;
  -- pre: none
  -- post: quotient of C1 & C2 is returned
  
  function get_real (C: in Complex) return Float;
  -- pre: none
  -- post: real of C is returned
  
  function get_imag (C: in Complex) return Float;
  -- pre: none
  -- post: imaginary of C is returned
  
  private
    type Complex is
      record
        Real: Float := 0.0;
        Imag: Float := 0.0;
      end record;
      
end Complex;
