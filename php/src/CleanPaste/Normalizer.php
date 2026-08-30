<?php

declare(strict_types=1);

namespace CleanPaste;

final class Normalizer
{
    private function __construct() {}

    public static function normalize(string $text): string
    {
        $text = str_replace(["\r\n", "\r"], "\n", $text);
        if (class_exists('Normalizer')) {
            $text = \Normalizer::normalize($text, \Normalizer::FORM_KC) ?? $text;
        }
        $text = strtr($text, [
            "\u{00A0}" => ' ', "\u{1680}" => ' ', "\u{2000}" => ' ',
            "\u{2001}" => ' ', "\u{2002}" => ' ', "\u{2003}" => ' ',
            "\u{2004}" => ' ', "\u{2005}" => ' ', "\u{2006}" => ' ',
            "\u{2007}" => ' ', "\u{2008}" => ' ', "\u{2009}" => ' ',
            "\u{200A}" => ' ', "\u{202F}" => ' ', "\u{205F}" => ' ',
            "\u{3000}" => ' ',
            "\u{200B}" => '', "\u{200C}" => '', "\u{200D}" => '',
            "\u{200E}" => '', "\u{200F}" => '', "\u{2060}" => '',
            "\u{FEFF}" => '',
        ]);
        $text = preg_replace('/[ \t]+\n/u', "\n", $text) ?? $text;
        return rtrim($text, " \t");
    }
}
