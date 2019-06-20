%define name zd1211-firmware

Summary: Firmware files for the ZD1211 chip
Name: %{name}
Version: 1.5
Release: 1
Source0: http://prdownloads.sourceforge.net/zd1211/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/zd1211/
BuildArch: noarch

%description
This package contains the firmware files for the ZD1211 chip, which is
used in WLAN USB sticks.
The files are generated from C header files distributed in the
original ZyDAS ZD1211 driver under the GNU Public License.
The full source of the original ZYDAS driver is available from
http://www.deine-taler.de/zd1211/

%prep
%setup -q -n %{name}

%build

%install
install -d $RPM_BUILD_ROOT/lib/firmware/zd1211
install -m644 zd1211* $RPM_BUILD_ROOT/lib/firmware/zd1211

%files
%doc README
/lib/firmware/zd1211/zd1211*
