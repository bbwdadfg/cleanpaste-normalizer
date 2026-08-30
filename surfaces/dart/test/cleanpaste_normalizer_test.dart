import 'package:cleanpaste_normalizer/cleanpaste_normalizer.dart';

void main() {
  final result = normalizePastedText('Ａ\u00a0B\u200b\r\nsecond line  \rfinal\t ');
  assert(result == 'A B\nsecond line\nfinal');
}
