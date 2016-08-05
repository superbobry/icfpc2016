open Num
open Core_kernel.Std

open Types

let n = num_of_int

let search skeleton =
  let open Figure in
  let rec go iter = function
  | [] -> failwith "Engine.search: problem too hard"
  | acc ->
    let candidates = List.concat_map acc ~f:(fun f ->
        List.filter_map (segments f) ~f:(unfold f))
    in match List.find candidates ~f:(fun f -> area f =/ n 1) with
    | Some solution -> solution
    | None -> begin
        printf "iter %04d: %d candidates\n" iter (List.length candidates);
        go (succ iter)
          (List.filter candidates ~f:(fun f -> area f </ n 1))
      end
  in go 0 [Figure.of_skeleton skeleton]


let () as _test_search1 =
  let a = (n 0, n 0)
  and b = (n 0, div_num (n 1) (n 2))
  and c = (n 1, div_num (n 1) (n 2))
  and d = (n 1, n 0) in

  let skeleton = [(a, b); (b, c); (c, d); (d, a)] in
  printf "1/2 square: %s\n" (Figure.show (search skeleton))


let () as _test_search2 =
  let h = div_num (n 1) (n 2) in
  let a = (n 0, n 0)
  and b = (n 0, h)
  and c = (h, h)
  and d = (n 1, n 0) in

  let skeleton = [(a, b); (b, c); (c, d); (d, a); (a, c)] in
  printf "spec. example: %s\n" (Figure.show (search skeleton))
