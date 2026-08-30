(ns cleanpaste.normalizer-test
  (:require [clojure.test :refer [deftest is run-tests]]
            [cleanpaste.normalizer :as normalizer]))

(deftest normalizes-pasted-text
  (is (= "A B\nsecond line\nfinal"
         (normalizer/normalize-pasted-text
          "Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t "))))

(defn -main [& _]
  (let [{:keys [fail error]} (run-tests 'cleanpaste.normalizer-test)]
    (System/exit (if (zero? (+ fail error)) 0 1))))
