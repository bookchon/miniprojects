using Bogus;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BogusTestApps.Models
{
    public class SampleCustomerRepository
    {
        public IEnumerable<Customer> GetCustomers(int genNum)
        {
            Randomizer.Seed = new Random(123456);
            // 아래와 같은 규칙으로 더미데이터를 생성
            var orderGen = new Faker<Order>()
                .RuleFor(o => o.Id, Guid.NewGuid)
                .RuleFor(o => o.Date, f => f.Date.Past(3)) // 날짜를 3년 전으로 세팅
                .RuleFor(o => o.OrderValue, f => f.Finance.Amount(1, 10000)) // 1부터 10000까지 숫자중에서 랜덤하게 세팅
                .RuleFor(o => o.Shipped, f => f.Random.Bool(0.8f)); // 0.5f면 true/false 반반

            // 고객 더미 데이터 생성 규칙
            var customerGen = new Faker<Customer>()
                .RuleFor(c => c.Id, Guid.NewGuid())
                .RuleFor(c => c.Name, f => f.Company.CompanyName())
                .RuleFor(c => c.Address, f => f.Address.FullAddress())
                .RuleFor(c => c.Phone, f => f.Phone.PhoneNumber())
                .RuleFor(c => c.ContactName, f => f.Name.FullName())
                .RuleFor(c => c.Orders, f => orderGen.Generate(f.Random.Number(1, 2)).ToList());

            return customerGen.Generate(genNum);
        }
    }
}
