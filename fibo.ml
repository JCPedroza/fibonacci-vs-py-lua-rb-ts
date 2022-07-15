(* Run me with: ocaml fibo.ml *)

(** Compute nth Fibonacci number using simple recursion. *)
let rec fibo_simple (index : int) : int =
  if index < 2
  then index
  else fibo_simple (index - 1) + fibo_simple (index - 2)

(** Compute nth Fibonacci number using simple recursion pattern matching. *)
let rec fibo_match (index: int) : int = match index with
  | 0 -> 0
  | 1 -> 1
  | x -> fibo_match (x - 1) + fibo_match (x - 2)

(** Compute nth Fibonacci number using tail recursion. *)
let fibo_tail (index : int) : int =
  let rec loop now nxt = function
    | 0 -> now
    | x -> loop nxt (now + nxt) (x - 1)
in loop 0 1 index

(** Compute nth Fibonacci number using memoization. *)
let fibo_memo (index : int) : int =
  let results = Array.make (index + 1) None in
  let rec loop index = match results.(index) with
    | Some result -> result
    | None -> let result =
      if index < 2
      then index
      else loop (index - 1) + loop (index - 2)
      in results.(index) <- Some result; result
  in loop index

let () = 6 |> fibo_simple |> string_of_int |> print_endline
let () = 6 |> fibo_match |> string_of_int |> print_endline
let () = 6 |> fibo_tail |> string_of_int |> print_endline
let () = 6 |> fibo_memo |> string_of_int |> print_endline
