%define		module	pymetar
Summary:	Module that provides access to NOAA's METAR weather reports
Summary(pl.UTF-8):	Moduł do pobierania danych pogodowych METAR
Name:		python-%{module}
Version:	0.13
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.schwarzvogel.de/pkgs/%{module}-%{version}.tar.gz
# Source0-md5:	84b6737b101daf5647a60d0d93d7783a
URL:		http://www.schwarzvogel.de/software-pymetar.shtml
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The National Oceanic and Atmospheric Administration (NOAA,
www.noaa.gov) provides easy access to the weather reports generated by
a large number of weather stations (mostly at airports) worldwide.
Those reports are called METAR reports and are delivered as plain text
files.

While this is convenient if you just want to quickly look up the data,
there's some effort involved in parsing all of this into a format that
is digestible by a program. Plus, you have to remember the base URL of
the reports and fetch the file.

The library provides a large number of methods to fetch the parsed
information in a plethora of formats. Those functions are described in
the file librarydoc.txt which was in turn generated using PyDoc.

%description -l pl.UTF-8
NOAA (Narodowa Administracja Oceaniczna i Atmosferyczna, www.noaa.gov)
udostępnia raporty pogodowe generowane przez wiele stacji pogodowych z
całego świata. Raporty te nazywane są raportami METAR i udostępniane w
postaci plików tekstowych.

Jest to wygodne jeśli chce się szybko przejrzeć dane. Jednak
przetwarzanie ich może być kłopotliwe. Dodatkowo, trzeba pamiętać
adres pliku z danej stacji pogodowej.

Biblioteka ta udostępnia wiele metod, które udostępniają dane
przetworzone z raportów METAR.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT --optimize=2

install bin/example.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{module}.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README THANKS TODO librarydoc.txt
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/*.py[co]
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
