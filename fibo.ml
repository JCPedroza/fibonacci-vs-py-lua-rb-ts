(* Run me with: ocaml fibo.ml *)

(* Compute nth Fibonacci number using simple recursion. *)
let rec fibo_simple index =
  if index < 2
  then index
  else fibo_simple (index - 1) + fibo_simple (index - 2)

let () = 6 |> fibo_simple |> string_of_int |> print_endline
