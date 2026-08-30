(ns cleanpaste.normalizer
  (:require [clojure.string])
  (:import [java.text Normalizer Normalizer$Form]))

(def ^:private zero-width
  ["\u200B" "\u200C" "\u200D" "\u200E" "\u200F" "\u202A" "\u202B"
   "\u202C" "\u202D" "\u202E" "\u2060" "\uFEFF"])

(def ^:private unicode-spaces
  ["\u00A0" "\u1680" "\u2000" "\u2001" "\u2002" "\u2003" "\u2004"
   "\u2005" "\u2006" "\u2007" "\u2008" "\u2009" "\u200A" "\u202F"
   "\u205F" "\u3000"])

(defn normalize-pasted-text [text]
  (when-not (string? text)
    (throw (IllegalArgumentException. "text must be a string")))
  (let [line-endings (-> text (.replace "\r\n" "\n") (.replace "\r" "\n"))
        compatibility (Normalizer/normalize line-endings Normalizer$Form/NFKC)
        without-zero-width (reduce #(clojure.string/replace %1 %2 "") compatibility zero-width)
        with-spaces (reduce #(clojure.string/replace %1 %2 " ") without-zero-width unicode-spaces)]
    (-> with-spaces
        (clojure.string/replace #"[ \t]+\n" "\n")
        (clojure.string/replace #"[ \t]+$" ""))))
