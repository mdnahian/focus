#!/usr/bin/perl

 my $dir = "./";

 opendir DH, $dir or die "Can't open  $dir: $!";
 $count2=1;
 while  ($name = readdir DH) {
  next unless $name =~ /\.mp3$/;
  $wav="$count2.wav";
   print "$wav\n";
system "mpg123 -w $wav \"$name\"";
  $count2++;
}
