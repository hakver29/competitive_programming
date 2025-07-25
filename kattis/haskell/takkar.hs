compareButtons :: Int -> Int -> String
compareButtons trump kim
  | trump > kim = "MAGA!"
  | trump < kim = "FAKE NEWS!"
  | otherwise   = "WORLD WAR 3!"

main :: IO ()
main = do
  trumpLine <- getLine
  kimLine <- getLine
  let trump = read trumpLine :: Int
      kim = read kimLine :: Int
  putStrLn (compareButtons trump kim)
