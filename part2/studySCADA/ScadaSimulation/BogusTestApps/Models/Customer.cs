using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BogusTestApps.Models
{
    public class Customer // 고객 테이블 매핑
    {
        public Guid Id { get; set; }
        public string Name { get; set; }
        public string Address { get; set; }
        public string Phone { get; set; }
        public string ContactName { get; set; }
        public IEnumerable<Order> Orders { get; set; }

    }
}
