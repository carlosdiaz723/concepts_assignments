with Complex, Ada.Text_IO, Ada.Float_Text_IO;
use Complex, Ada.Text_IO, Ada.Float_Text_IO;

-- Carlos Diaz
-- Source for Ada Assignment

procedure Test_Complex is

  C1, C2: Complex.Complex;
  A, B, C, D: Float;

  procedure display_complex (c: in Complex.Complex) is
    begin
        put(get_real(C => c), Fore => 2, Aft => 2, Exp => 0);
        put(" + ");
        put(get_imag(C => c), Fore => 2, Aft => 2, Exp => 0);
        put("i");
    end display_complex;
  
  begin
    Ada.Text_IO.Put("Enter real part of first number: ");
    Ada.Float_Text_IO.Get(A);
    Ada.Text_IO.Put("Enter imaginary part of first number: ");
    Ada.Float_Text_IO.Get(B);
    Ada.Text_IO.Put("Enter real part of second number: ");
    Ada.Float_Text_IO.Get(C);
    Ada.Text_IO.Put("Enter imaginary part of second number: ");
    Ada.Float_Text_IO.Get(D);

    C1 := Create_Complex(R => A, I => B);
    C2 := Create_Complex(R => C,  I => D);
    put("Addition:  ");
    display_complex (c => C1 + C2);
    New_Line;
    put("Subtraction:  ");
    display_complex (c => C1 - C2);
    New_Line;
    put("Multiplication:  ");
    display_complex (c => C1 * C2);
    New_Line;
    put("Division:  ");
    display_complex (c => C1 / C2);
    New_Line;
  end Test_Complex;
