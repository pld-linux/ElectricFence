Summary:	A debugger which detects memory allocation violations
Summary(de):	Debugger zum Erkennen von Speicherzugriffsverletzungen
Summary(es):	Electric Fence biblioteca de depuración de memoria en C
Summary(fr):	Bibliothèque C de débuggage mémoire Electric Fence
Summary(pl):	Biblioteka do wykrywania b³edów alokacji pamiêci
Summary(pt):	Electric Fence biblioteca de depuração de memória em C
Summary(tr):	C için bellek hatasý ayýklama kitaplýðý
Name:		ElectricFence
Version:	2.2.2
Release:	6
License:	GPL
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source0:	ftp://ftp.perens.com/pub/ElectricFence/Beta/%{name}-%{version}.tar.gz
Patch0:		%{name}-longjmp.patch
Patch1:		%{name}-no_bash.spec
Patch2:		%{name}-va_arg.patch
Patch3:		%{name}-ac_am.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you know what malloc() violations are, you'll be interested in
ElectricFence. ElectricFence is a tool which can be used for C
programming and debugging. It uses the virtual memory hardware of your
system to detect when software overruns malloc() buffer boundaries,
and/or to detect any accesses of memory released by free().
ElectricFence will then stop the program on the first instruction that
caused a bounds violation and you can use your favorite debugger to
display the offending statement.

%description -l de
Wenn Sie wissen, was malloc()-Verletzungen sind, sind Sie
wahrscheinlich an ElectricFence interessiert. ElectricFence ist ein
Tool, das zur C- Programmierung und zum Debugging benutzt werden kann.
Es benutzt virtuelle Speicherhardware, um zu erkennen, wenn Software
malloc()-Buffergrenzen übersteigt, und wenn Speicher mit free()
freigegeben wird. ElectricFence beendet das Programm bei der
Instruktion, die die Speicherverletzung ausgelöst hat, und Sie können
Ihren Lieblingsdebugger benutzen, um den Befehl anzuzeigen.

%description -l es
Electric Fence es una biblioteca que puede ser usada para programación
y depuración en C. Tu lo "linkas" en tiempo de compilación y te
avisará sobre posibles problemas, como liberación de memoria no
alocada, etc.

%description -l fr
Electric Fence est une bibliothéque utilisée pour la programmation en
C et le débogage. Vous pouvez la lier à la compilation et elle vous
avertira des problèmes éventuels de désallocation de mémoire, etc.

%description -l pl
Electric Fence jest bibliotek± pomocn± podczas programowania w jêzyku
C i "odpluskwianiu". Pakiet zawiera bibliotekê wspó³dzielon±, która
mo¿e byæ za³adowana przez zmienn± LD_PRELOAD w trakcie uruchamiania
dowolnego programu dziêki temu nie potrzeba linkowaæ z t± bibliotek±
¶ledzonego programu. Pakiet zawiera tak¿e skrypt pow³oki ef, który
³aduje do pamiêci przez LD_PRELOAD bibliotekê libefence i uruchamia
program przekazany do tego skryptu jako parametr.

%description -l pt
Electric Fence é uma biblioteca que pode ser usada para programação e
depuração em C. Você o "linka" em tempo de compilação e ele o avisará
sobre possíveis problemas como liberação de memória não alocada, etc.

%description -l tr
Electric Fence, C'de programlama ve hata ayýklama için kullanýlabilen
bir kitaplýktýr. Derleme esnasýnda programýnýza baðlarsanýz, sizi
ortaya çýkabilecek sorunlar (var olmayan bir bellek parçasýnýn serbest
býrakýlmasý gibi) konusunda uyarýr.

%package static
Summary:	Satatic Electric Fence library
Summary(pl):	Biblioteka statyczna Electric Fence
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze

%description static
Satatic Electric Fence library.

%description -l pl static
Biblioteka statyczna Electric Fence.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
libtoolize --copy --force
automake -a -c
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/ef
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
