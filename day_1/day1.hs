import Data.List
import Data.Char

readAndPrint :: FilePath -> IO()
readAndPrint fileP = do
  input <- readFile fileP
  print $ sum $ numbers $ lines input

numbers :: [String] -> [Int]
numbers [] = []
numbers (s:ss) = [getInt [head (extractNumbers s), last (extractNumbers s)]] ++ numbers ss

nonDigit :: Char -> Bool
nonDigit = not . isDigit

  
extractNumbers :: String -> [Int]
extractNumbers [] = []
extractNumbers xs = do
  let afterDroppingNonDigits = dropWhile nonDigit xs
  let num = take 1 afterDroppingNonDigits
  if num == [] then []
  else [read num :: Int] ++ extractNumbers (drop 1 afterDroppingNonDigits)

getInt :: [Int] -> Int
getInt (x:xs) = do
  read (concat (map show (x:xs))) :: Int

-- Part 2
extNum :: String -> [Int]
extNum (c:s) 
  | "one" `isPrefixOf` (c:s) || "1" `isPrefixOf` (c:s) = [1] ++ extNum s
  | "two" `isPrefixOf` (c:s) || "2" `isPrefixOf` (c:s) = [2] ++ extNum s
  | "three" `isPrefixOf` (c:s) || "3" `isPrefixOf` (c:s) = [3] ++ extNum s
  | "four" `isPrefixOf` (c:s) || "4" `isPrefixOf` (c:s) = [4] ++ extNum s
  | "five" `isPrefixOf` (c:s) || "5"`isPrefixOf` (c:s) = [5] ++ extNum s
  | "six" `isPrefixOf` (c:s) || "6" `isPrefixOf` (c:s) = [6] ++ extNum s
  | "seven" `isPrefixOf` (c:s) || "7" `isPrefixOf` (c:s) = [7] ++ extNum s
  | "eight" `isPrefixOf` (c:s) || "8" `isPrefixOf` (c:s) = [8] ++ extNum s
  | "nine" `isPrefixOf` (c:s) || "9" `isPrefixOf` (c:s) = [9] ++ extNum s
extNum (c:s) = extNum s
extNum [] = []

numbers2 :: [String] -> [Int]
numbers2 [] = []
numbers2 (s:ss) = do
  let nums = extNum s
  [getInt [head nums, last nums]] ++ numbers2 ss

readAndPrint2 :: FilePath -> IO()
readAndPrint2 fileP = do
  input <- readFile fileP
  print $ sum $ numbers2 $ lines input


